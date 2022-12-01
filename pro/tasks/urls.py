from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.list , name='list'),
    path('update_task/<int:pk>/' , views.updateTask , name ='update_task'),
    path('delete/<int:pk>/',views.deleteTask,name = 'delete'),
]

