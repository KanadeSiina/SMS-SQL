"""SMS-SQL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from login import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
    path('select/', views.select),
    path('student_table/', views.student_table),
    path('teacher_table/', views.teacher_table),
    path('drop_course/', views.drop_course),
    path('ScoreQuery/', views.score_query),
    path('Giveup/', views.give_up),
    path('Course/', views.course_table, name='Course'),
    re_path(r'^Course/InputScore/(\d+)/', views.input_score, name='InputScore'),
    path('Open/', views.open_course),
]