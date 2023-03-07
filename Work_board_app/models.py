from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime
from django.db.models import OuterRef, Subquery, Prefetch, QuerySet

TODAY_DATETIME = datetime.today()
TODAY_DATE = TODAY_DATETIME.date()

class CustomUser(AbstractUser):
    # 拡張
    class Meta:
        db_table = 'cutom_user'
    comment = models.TextField(verbose_name='コメント', blank=True)


class Work_time(models.Model):
    class Meta:
        db_table = 'work_time'
    target_user = models.ForeignKey(CustomUser, on_delete=models.PROTECT, verbose_name='対象者', max_length=100)
    attendance_date = models.DateField(verbose_name='出勤日')
    start_work_time = models.DateTimeField(verbose_name='開始時刻', null=True)
    end_work_time = models.DateTimeField(verbose_name='退勤時刻', null=True)

    # 当日の勤怠情報を取得
    def get_today_info(queryset):
        queryset = CustomUser.objects.annotate(start_work_time=Subquery(Work_time.objects.filter(
            target_user=OuterRef('pk'), attendance_date=TODAY_DATE).values('start_work_time')
        ))
        queryset = queryset.annotate(end_work_time=Subquery(Work_time.objects.filter(
            target_user=OuterRef('pk'), attendance_date=TODAY_DATE).values('end_work_time')
        ))
        queryset = queryset.annotate(work_time_id=Subquery(Work_time.objects.filter(
            target_user=OuterRef('pk'), attendance_date=TODAY_DATE).values('id')
        ))

        return queryset.order_by('-date_joined')



