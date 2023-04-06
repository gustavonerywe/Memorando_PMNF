from . import views
from django.urls import path

urlpatterns = [
    path('upload/', views.upload, name='upload'),
    path('upload_success/', views.file_list, name='file_list'),
    path('file_detail<int:pk>.html', views.file_detail, name='file_detail'),
    path('upload.html', views.upload, name='upload-html'),
]
