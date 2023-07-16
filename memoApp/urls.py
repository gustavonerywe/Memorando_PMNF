from . import views
from django.urls import path

urlpatterns = [
    path('', views.upload, name='upload'),
    path('upload_success/<id>', views.file_detail, name='file_detail'),
    path('generate_pdf/<int:id_criptografado>', views.generate_pdf, name='generate_pdf'),
    path('generate_pdf_circular/<int:id_criptografado>', views.generate_pdf_circular, name='generate_pdf_circular'),
    path('login/', views.loginPage, name='loginPage'),
    path('encerrar-sessao/', views.encerraSessao, name='encerraSessao'),
    path('gerar-pdf/<int:id_criptografado>/', views.geraEBaixaPDF, name='gerar_pdf'),
    path('gerar-pdf-circular/<int:id_criptografado>/', views.geraEBaixaPDFCircular, name='gerar_pdf_circular'),
    path('force-download/', views.force_download, name='force_download'),
    path('my-pdf/<int:pk>/', views.PrintView.as_view(), name='my_pdf'),
    path('memorando_circular', views.memorando_circular, name='memorando_circular')
]
