from typing import Any
from django.shortcuts import render, redirect,  get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django import forms
from .models import *
from django.http import Http404, FileResponse, HttpResponse
from .forms import ImageForm
from django.utils import timezone
import datetime
from bs4 import BeautifulSoup
from django.utils.html import strip_tags
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import Group
from django.contrib.sessions.backends.db import SessionStore
from django.utils.safestring import mark_safe
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
import os
from django.shortcuts import get_object_or_404
from django.conf import settings
from io import BytesIO
from pathlib import Path
from django.template.loader import render_to_string
# from urllib.parse import quote
from weasyprint import HTML, CSS
from django_weasyprint import *


BASE_DIR = Path(__file__).resolve().parent.parent

@login_required
def upload(request):
    grupos = Group.objects.all()
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            memorando = Memorando()
            memorando.assunto = request.POST.get('assunto_memorando')
            memorando.corpo = request.POST.get('corpo')
            memo_numero_atualizado = memorando.gerar_proximo_numero()
            memorando.data = request.POST.get('data')
            memorando.remetente = request.user
            memorando.memo_numero = memo_numero_atualizado
            grupo_escolhido = request.POST.getlist('destinatario')
            if grupo_escolhido[0] == 'Todos':
                todosGrupos = []
                for grupo in grupos:
                    todosGrupos.append(grupo.name)
                grupo_escolhido = todosGrupos    
                
            grupo_escolhido_copia = request.POST.getlist('destinatarios_copia')
            try:
                if grupo_escolhido_copia[0] == 'Todos':
                 todosGrupos = []
                 for grupo in grupos:
                    todosGrupos.append(grupo.name)
                 grupo_escolhido_copia = todosGrupos    
            except:
                pass
                
            session = SessionStore(request.session.session_key)
            session['grupo_escolhido'] = grupo_escolhido
            session['memorando_corpo'] = memorando.corpo
            session['grupo_escolhido_copia'] = grupo_escolhido_copia
            session.save()

            memorando.save()

            for file in request.FILES.getlist('file'):
                image = Image.objects.create(file=file)
                image.memorando = memorando
                image.save()

            context = {
                'memorando': memorando,
                'memo_numero_atualizado': memo_numero_atualizado,
                'memorando_corpo': mark_safe(memorando.corpo),
                'memorando_remetente': memorando.remetente,
                'memorando_assunto': memorando.assunto,
                'grupos': grupos,
            }
            return render(request, 'upload_success.html', context)
    else:
        form = ImageForm()

    context = {
        'form': form,
        'memo_numero_atualizado': Memorando().gerar_proximo_numero(),
        'memorando_corpo': Memorando().corpo,
        'grupos': grupos,
    }
    return render(request, 'memo_main.html', context)


@login_required
def generate_pdf(request, id_criptografado):
    memorando = Memorando.objects.get(id=id_criptografado)
    memo_numero_atualizado = memorando.gerar_proximo_numero()
    data_atual = datetime.date.today()
    data_numerica = data_atual.strftime("%d/%m/%y")
    session = SessionStore(request.session.session_key)
    grupo_escolhido = session.get('grupo_escolhido')
    text_content = session.get('memorando_corpo')
    grupo_escolhido_copia = session.get('grupo_escolhido_copia')
    context = {
        'memorando': memorando,
        'memo_numero_atualizado': memo_numero_atualizado,
        'memorando_assunto': memorando.assunto,
        'data_atual': data_numerica,
        'grupo_escolhido': grupo_escolhido,
        'text_content': mark_safe(text_content),
        'grupo_escolhido_copia': grupo_escolhido_copia,
    }
    print(grupo_escolhido_copia)
    return render(request, 'generate_pdf.html', context)



@login_required
def data_atual(request):
    data = datetime.date.today()
    context ={
        'data': data
    }
    return render(request, 'memo_main.html', context)

from django.core.exceptions import SuspiciousFileOperation

from django.core.exceptions import SuspiciousFileOperation

@login_required
def file_detail(request, id):
    try:
        image = Image.objects.get(id=id)
        if not image.file:
            raise SuspiciousFileOperation("Image file not found")
        
        image_size_kb = round(image.file.size / 1024)
        image_size_mb = round(image_size_kb / 1024, 2)
        timestamp = timezone.now()
    except Image.DoesNotExist:
        raise Http404("Image does not exist")
    except SuspiciousFileOperation:
        raise Http404("Image file not found")

    try:
        # Calcular a soma dos tamanhos de todos os arquivos
        total_size_mb = 0
        images = Image.objects.filter(file=image.file)
        for img in images:
            if img.file:
                total_size_mb += round(img.file.size / (1024 * 1024), 2)
    except FileNotFoundError:
        total_size_mb = 0

    context = {
        'image': image,
        'image_size_mb': image_size_mb,
        'timestamp': timestamp,
        'total_size_mb': total_size_mb
    }

    return render(request, 'upload_success.html', context)




        

@login_required
def digital_view(request, id):
    try: 
        image = Image.objects.get(id=id)
        # with open(str(image.file), 'rb') as pdf_file:
        #     pdf_reader = PyPDF2.PdfReader(pdf_file)
        #     num_pages = len(pdf_reader.pages)
        #     for page_num in range(num_pages):
        #         page = pdf_reader.pages[page_num]
        #         print(page.extract_text())
    except Image.DoesNotExist:
        raise Http404("Image does not exist")
    
    return JsonResponse(str(image.file), safe=False)

@login_required
def file_list(request):
    files = Image.objects.all()
    return render(request, 'upload_success.html', {'files': files})


def loginPage(request):
    if request.user.is_authenticated:
        return render(request, 'login.html', {'logado': True})
    else:
        if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:        
                    login(request, user)
                    return redirect('upload')
                    # Redirect to a success page
        else:
            form = AuthenticationForm(request)
        return render(request, 'login.html', {'form': form})
    
    
def encerraSessao(request):
    logout(request)
    return redirect('loginPage')

# def geraEBaixaPDF(request, id_criptografado):
#     pdf = pdfkit.from_url('http://localhost:8000/generatepdf/' + str(id_criptografado))
#     response = FileResponse(pdf, as_attachment=True, filename='memorando.pdf')
#     return response

import io
from django.http import HttpResponse


def geraEBaixaPDF(request, id_criptografado):
    
    # id_criptografado_criptografado = criptografar_id_criptografado(id_criptografado)
    # url_criptografada = quote(id_criptografado_criptografado)
    memorando = Memorando.objects.get(id=id_criptografado)
    data_atual = datetime.date.today()
    data_numerica = data_atual.strftime("%d/%m/%y")
    session = SessionStore(request.session.session_key)
    grupo_escolhido = session.get('grupo_escolhido')
    text_content = session.get('memorando_corpo')
    grupo_escolhido_copia = session.get('grupo_escolhido_copia')
    context = {
        'memorando': memorando,
        'memorando_assunto': memorando.assunto,
        'data_atual': data_numerica,
        'grupo_escolhido': grupo_escolhido,
        'text_content': mark_safe(text_content),
        'grupo_escolhido_copia': grupo_escolhido_copia,
    }
    
    
    html_path = str(BASE_DIR) + "/memoApp/templates/generate_pdf.html"

    # path_wkhtmltopdf = 'C:\Program Files\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
    # output_pdf = str(BASE_DIR)+'\\pdf_criado.pdf'
    html_render = render_to_string('generate_pdf.html', context, request=request)
    
    # config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    pathToPdf = str(BASE_DIR)+'/pdfs/memorando' + str(id_criptografado) + '.pdf'
    
    # HTML(string=html_render).write_pdf(pathToPdf, stylesheets=[CSS(filename=str(BASE_DIR)+'/memoApp/static/css/style.css')])
    
    
    with open(pathToPdf, 'rb') as f:
            response = HttpResponse(f, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="memorando.pdf"'
            return response
    

@login_required
def force_download(request, pdf):
    # file_path = str(BASE_DIR) + '/memoApp/static/teste.txt'
    with BytesIO(pdf) as f:
            response = HttpResponse(f, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="memorando.pdf"'
            return response
        
from django.views.generic import DetailView

from django_weasyprint import WeasyTemplateResponseMixin


class MyDetailView(DetailView):
    template_name = 'generate_pdf.html'


class PrintView(WeasyTemplateResponseMixin, MyDetailView):
    
    model = Memorando
    
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        
    def get_queryset(self):
        return Memorando.objects.all()
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        memorando = Memorando.objects.get(id=self.kwargs['pk'])
        data_atual = datetime.date.today()
        data_numerica = data_atual.strftime("%d/%m/%y")
        session = SessionStore(self.request.session.session_key)
        grupo_escolhido = session.get('grupo_escolhido')
        text_content = session.get('memorando_corpo')
        grupo_escolhido_copia = session.get('grupo_escolhido_copia')
        context = {
            'memorando': memorando,
            'memorando_assunto': memorando.assunto,
            'data_atual': data_numerica,
            'grupo_escolhido': grupo_escolhido,
            'text_content': mark_safe(text_content),
            'grupo_escolhido_copia': grupo_escolhido_copia,
        }
        
        
        return context

    pdf_stylesheets= [
        settings.STATIC_ROOT + '/css/style.css',
    ]
    
    pdf_filename = 'memo.pdf'
    
    response_class = WeasyTemplateResponse
    

import hashlib

# def criptografar_id_criptografado(id_criptografado):
#     id_criptografado_str = str(id_criptografado)
    
#     hash_object = hashlib.sha256(id_criptografado_str.encode())
#     encrypted_id = hash_object.hexdigest()
    
#     return encrypted_id