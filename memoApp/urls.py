from . import views
from django.urls import path

urlpatterns = [
    path('', views.upload, name='upload'),
    path('upload_success/<id>', views.file_detail, name='file_detail'),
]
