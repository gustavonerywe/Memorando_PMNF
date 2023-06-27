from . import views
from django.urls import path

urlpatterns = [
    path('', views.upload, name='upload'),
    path('upload_success/<id>', views.file_detail, name='file_detail'),
    path('generate_pdf/<int:memorando_id>', views.generate_pdf, name='generate_pdf'),
    path('login/', views.loginPage, name='loginPage'),
]
