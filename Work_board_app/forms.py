from django import forms
from .models import CustomUser,Work_time

# class CustomUserForm(forms.ModelForm):
#     class Meta:
#         model = CustomUser
#         comment = forms.Textarea(class="")
#         fields = ('comment',)
        
# class CustomUserForm(forms.Form):
#     # comment = forms.Textarea(attrs={"rows": "4"})
#     comment = forms.CharField(widget=forms.Textarea,)

class Work_timeForm(forms.ModelForm):
    class Meta:
        model = Work_time
        fields = ['target_user','attendance_date','start_work_time','end_work_time']

