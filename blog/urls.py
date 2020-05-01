from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.allblog,name='allblog'),
    path('<int:blog_id>',views.detail,name='detail'),
]
