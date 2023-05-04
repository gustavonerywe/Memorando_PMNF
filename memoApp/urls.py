from . import views
from django.urls import path

urlpatterns = [
    path('', views.upload, name='upload'),
    path('upload_success/', views.file_list, name='file_list'),
    path('file_detail/<id>', views.file_detail, name='file_detail'),
    path('digital_view/<id>', views.digital_view, name='digital_view'),
]
