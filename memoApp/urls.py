from . import views
from django.urls import path

urlpatterns = [
    path('upload.html', views.upload, name='upload'),
     path('file/<int:pk>/', views.file_detail, name='file_detail'),
]