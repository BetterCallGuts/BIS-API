from django.urls import path
from .           import views


urlpatterns = [
    path('allstudent/', views.getallstudent, name='index'),
    path('allparent/', views.getallparent, name='index'),
    path('alldata/', views.getalldata, name='index'),
    
]
