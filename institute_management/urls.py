from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('base',base_page,name='base_page'),
    path('',index_page,name='index_page'),
    path('login',login_page,name='login_page'),
]