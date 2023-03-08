from django.shortcuts import render
from django.views.generic import ListView, FormView, CreateView, UpdateView
from django.db.models import OuterRef, Subquery, Prefetch
from .models import CustomUser, Work_time
from .forms import Work_timeForm
from datetime import datetime

TODAY_DATETIME = datetime.today()
TODAY_DATE = TODAY_DATETIME.date()

# 初期画面表示
class Home_view(ListView):
    template_name = 'home.html'
    model = CustomUser

    def get_queryset(self):
        queryset = super().get_queryset()
        return Work_time.get_today_info(queryset)

# 伝言の更新
class Message_update_view(ListView):
    template_name = 'home.html'
    model = CustomUser

    def post(self, request, *args, **kwargs):
        cmnt = self.request.POST.get("comment")
        customuser = CustomUser(id=self.kwargs['pk'])
        customuser.comment = cmnt
        # 更新はコメントだけ
        customuser.save(update_fields=['comment'])
        return self.get(request, *args, **kwargs)
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return Work_time.get_today_info(queryset)

# 出勤時刻登録
class Workstart_register_view(ListView):
    template_name = 'home.html'
    model = CustomUser

    def post(self, request, *args, **kwargs):
        customuser = CustomUser.objects.get(id=self.kwargs['pk'])
        work_time = Work_time.objects.filter(attendance_date=TODAY_DATE, start_work_time=TODAY_DATETIME, target_user=customuser)
        
        if work_time.exists():
            pass
        else:
            Work_time.objects.create(attendance_date=TODAY_DATE, start_work_time=TODAY_DATETIME, target_user=customuser)
 
        return self.get(request, *args, **kwargs)
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return Work_time.get_today_info(queryset)

# 退勤時刻登録
class Workend_register_view(ListView):
    template_name = 'home.html'
    model = CustomUser

    def post(self, request, *args, **kwargs):
        # customuser = CustomUser.objects.get(id=self.kwargs['pk'])
        work_time = Work_time.objects.get(id=self.kwargs['pk'])
        work_time.end_work_time = TODAY_DATETIME
        work_time.save(update_fields=['end_work_time'])
        return self.get(request, *args, **kwargs)
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return Work_time.get_today_info(queryset)

