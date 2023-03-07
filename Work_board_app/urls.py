
from django.contrib import admin
from django.urls import path,include
from .views import Home_view,Message_update_view,Workstart_register_view,Workend_register_view

import debug_toolbar

urlpatterns = [
    path('',Home_view.as_view(),name="home"),
    path('comment_update/<int:pk>',Message_update_view.as_view(),name="cmnt_update"),
    path('registed_workstart/<int:pk>',Workstart_register_view.as_view(),name="regist_workstart"),
    path('registed_workend/<int:pk>',Workend_register_view.as_view(),name="regist_workend"),

]


