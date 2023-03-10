from django.contrib import admin
from django.urls import path,include
from .views import data,update_1,delete_1

urlpatterns = [
    path('create',data.as_view(),name='create'),
    path('update/<int:pk>',update_1.as_view(),name='update'),
    path('delete/<int:pk>',delete_1.as_view(),name='delete'),
]
