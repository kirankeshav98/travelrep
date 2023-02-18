from . import views
from django.urls import path

urlpatterns = [
    path('',views.demo,name='demo'),
    # path('add/',views.addition,name='addition'),
    # path('content/',views.content,name='content')
]