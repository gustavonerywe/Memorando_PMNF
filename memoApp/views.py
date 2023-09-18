from typing import Any
from django.shortcuts import render, redirect,  get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django import forms
from .models import *
from django.http import Http404, FileResponse, HttpResponse
from .forms import ImageForm, SearchForm
from django.utils import timezone
import datetime
from bs4 import BeautifulSoup
from django.utils.html import strip_tags
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import Group
from django.contrib.sessions.backends.db import SessionStore
from django.utils.safestring import mark_safe
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
import os
from django.shortcuts import get_object_or_404
from django.conf import settings
from io import BytesIO
from pathlib import Path
from django.template.loader import render_to_string
# from urllib.parse import quote
from weasyprint import HTML, CSS, Attachment
from django_weasyprint import *
# import aspose.pdf as aspose
from reportlab.pdfgen import canvas
from PIL import Image as imgpil
from django.forms.utils import ErrorDict


BASE_DIR = Path(__file__).resolve().parent.parent

@login_required
def upload(request):
    grupos = Group.objects.all()
    groupuser = request.user.groups.first()
    groupaddress = GroupMoc.objects.get(group=groupuser)
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
            grupo_escolhido_copia = request.POST.getlist('destinatarios_copia')
            
            for i in range(grupo_escolhido.count('-- Selecione um grupo --')):
                   grupo_escolhido.remove('-- Selecione um grupo --')
            for i in range(grupo_escolhido_copia.count('-- Selecione um grupo --')):
                   grupo_escolhido_copia.remove('-- Selecione um grupo --')
                       
            memorando.save()
            
            for i in range(len(grupo_escolhido)):
                grupoDestinado = Group.objects.get(name=grupo_escolhido[i])
                memorando.destinatario.add(grupoDestinado)
            for i in range(len(grupo_escolhido_copia)):
                grupoDestinado = Group.objects.get(name=grupo_escolhido_copia[i])
                memorando.destinatarios_copia.add(grupoDestinado)
                
            files = request.FILES.getlist('file')
            
            nomesArquivos = []
            
            
            for file in files:
                file.name = str(datetime.date.today()) + "-" + file.name
                fileName = file.name
                caminho_completo = os.path.join(BASE_DIR, 'fileStorage', fileName)
                caminho_completo = caminho_completo.replace('\\', '/')
                nomesArquivos.append(caminho_completo)
                
            # print(caminho_completo)
                  
            session = SessionStore(request.session.session_key)
            session['grupo_escolhido'] = grupo_escolhido
            session['memorando_corpo'] = memorando.corpo
            session['grupo_escolhido_copia'] = grupo_escolhido_copia
            session['file_name'] = nomesArquivos
            session.save()

            for file in files:
                try:
                    with imgpil.open(file) as image:
                        image.save(f'fileStorage/{file.name}')
                except ValueError as e:
                    return redirect('erro')
            
            memorando.save()
            
            for file in files:
                anexo = Image()
                anexo.file = file
                anexo.idDoc = memorando.id
                anexo.tipoDoc = 'memorando'
                anexo.save()
                
            memorando.save()

            context = {
                'memorando': memorando,
                'memo_numero_atualizado': memo_numero_atualizado,
                'memorando_corpo': mark_safe(memorando.corpo),
                'memorando_remetente': memorando.remetente,
                'memorando_assunto': memorando.assunto,
                'grupos': grupos,
                'usermoc': UserMoc.objects.get(user=request.user),
                'grupomoc': groupaddress,
            }
            return render(request, 'upload_success.html', context)
    else:
        form = ImageForm()
    
    context = {
        'form': form,
        'memo_numero_atualizado': Memorando().gerar_proximo_numero(),
        'memorando_corpo': Memorando().corpo,
        'grupos': grupos,
        'usermoc': UserMoc.objects.get(user=request.user),
        'grupomoc': groupaddress,
    }
    return render(request, 'memo_main.html', context)

@login_required
def memorando_circular(request):
    grupos = Group.objects.all()
    memorandocircular = MemorandoCircular()
    groupuser = request.user.groups.first()
    groupaddress = GroupMoc.objects.get(group=groupuser)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            memorandocircular.assunto_circular = request.POST.get('assunto_memorando')
            memorandocircular.corpo_circular = request.POST.get('corpo')
            memo_numero_atualizado_circular = memorandocircular.gerar_proximo_numero_circular()
            memorandocircular.data_circular = request.POST.get('data')
            memorandocircular.remetente_circular = request.user
            memorandocircular.memo_numero_circular = memo_numero_atualizado_circular

            files = request.FILES.getlist('file')
            
            nomesArquivos = []
            
            
            for file in files:
                file.name = str(datetime.date.today()) + file.name
                fileName = file.name
                caminho_completo = os.path.join(BASE_DIR, 'fileStorage', fileName)
                caminho_completo = caminho_completo.replace('\\', '/')
                nomesArquivos.append(caminho_completo)
                
                
            session = SessionStore(request.session.session_key)
            session['memorando_corpo_circular'] = memorandocircular.corpo_circular
            session['file_name'] = nomesArquivos
            session.save()

            memorandocircular.save()

            for file in files:
                anexo = Image()
                anexo.file = file
                anexo.idDoc = memorandocircular.id
                anexo.tipoDoc = 'memorando-circular'
                anexo.save()
                
            memorandocircular.save()

            for file in files:
                with imgpil.open(file) as image:
                    image.save(f'fileStorage/{file.name}')


            context = {
                'memorandocircular': memorandocircular,
                'memo_numero_atualizado_circular': memorandocircular.memo_numero_circular,
                'memorando_corpo_circular': mark_safe(memorandocircular.corpo_circular),
                'memorando_remetente_circular': memorandocircular.remetente_circular,
                'memorando_assunto_circular': memorandocircular.assunto_circular,
                'grupos': grupos,
                'usermoc': UserMoc.objects.get(user=request.user),
                'grupomoc': groupaddress,
            }
            return render(request, 'upload_success_circular.html', context)
    else:
        form = ImageForm()

    context = {
    'form': form,
    'memo_numero_atualizado_circular': memorandocircular.gerar_proximo_numero_circular(),
    'memorando_corpo': Memorando().corpo,
    'grupos': grupos,
    'usermoc': UserMoc.objects.get(user=request.user),
    'grupomoc': groupaddress,
}

    return render(request, 'memorando_circular.html', context)


@login_required
def oficio(request):
    oficio = Oficio()
    groupuser = request.user.groups.first()
    groupaddress = GroupMoc.objects.get(group=groupuser)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            oficio.assunto_oficio = request.POST.get('assunto_memorando')
            oficio.corpo_oficio = request.POST.get('corpo')
            oficio_numero_atualizado = oficio.gerar_proximo_numero_oficio()
            oficio.data_oficio = request.POST.get('data')
            oficio.remetente_oficio = request.user
            oficio.memo_numero_oficio = oficio_numero_atualizado
            oficio.destinatario_oficio = request.POST.get('para-oficio')
            oficio.destinatarios_copia_oficio = request.POST.get('copia-oficio')

            files = request.FILES.getlist('file')
            
            nomesArquivos = []
            
            
            for file in files:
                file.name = str(datetime.date.today()) + file.name
                fileName = file.name
                caminho_completo = os.path.join(BASE_DIR, 'fileStorage', fileName)
                caminho_completo = caminho_completo.replace('\\', '/')
                nomesArquivos.append(caminho_completo)
                
                
            session = SessionStore(request.session.session_key)
            session['memorando_corpo'] = oficio.corpo_oficio
            session['file_name'] = nomesArquivos
            session.save()

            oficio.save()

            for file in files:
                anexo = Image()
                anexo.file = file
                anexo.idDoc = oficio.id
                anexo.tipoDoc = 'oficio'
                anexo.save()
                
            oficio.save()

            for file in files:
                with imgpil.open(file) as image:
                    image.save(f'fileStorage/{file.name}')
            
           
            context = {
                'oficio': oficio,
                'memo_numero_atualizado': oficio_numero_atualizado,
                'oficio_corpo': mark_safe(oficio.corpo_oficio),
                'oficio_remetente': oficio.remetente_oficio,
                'oficio_assunto': oficio.assunto_oficio,
                'destinatario_oficio': oficio.destinatario_oficio,
                'destinatario_copia_oficio': oficio.destinatarios_copia_oficio,
                'usermoc': UserMoc.objects.get(user=request.user),
                'grupomoc': groupaddress,
            }
            return render(request, 'upload_success_oficio.html', context)
    else:
        form = ImageForm()

    context = {
        'form': form,
        'memo_numero_atualizado_oficio': oficio.gerar_proximo_numero_oficio(),
        'memorando_corpo': Memorando().corpo,
        'usermoc': UserMoc.objects.get(user=request.user),
        'grupomoc': groupaddress,
    }
    return render(request, 'oficio.html', context)


@login_required
def generate_pdf(request, id_criptografado):
    grupos = Group.objects.all()
    memorando = Memorando.objects.get(id=id_criptografado)
    memo_numero_atualizado = memorando.gerar_proximo_numero()
    data_atual = datetime.date.today()
    data_numerica = data_atual.strftime("%d/%m/%y")
    session = SessionStore(request.session.session_key)
    grupo_escolhido = session.get('grupo_escolhido')
    text_content = session.get('memorando_corpo')
    grupo_escolhido_copia = session.get('grupo_escolhido_copia')
    usermoc = UserMoc.objects.get(user=memorando.remetente)
    context = {
        'memorando': memorando,
        'memo_numero_atualizado': memo_numero_atualizado,
        'memorando_assunto': memorando.assunto,
        'data_atual': data_numerica,
        'grupo_escolhido': grupo_escolhido,
        'text_content': mark_safe(text_content),
        'grupo_escolhido_copia': grupo_escolhido_copia,
        'usermoc': usermoc,
    }
    return render(request, 'generate_pdf.html', context)

@login_required
def generate_pdf_circular(request, id_criptografado):
    grupos = Group.objects.all()
    memorandocircular = MemorandoCircular.objects.get(id=id_criptografado)
    memo_numero_atualizado = memorandocircular.gerar_proximo_numero_circular()
    data_atual = datetime.date.today()
    data_numerica = data_atual.strftime("%d/%m/%y")
    session = SessionStore(request.session.session_key)
    grupo_escolhido = session.get('grupo_escolhido')
    text_content = session.get('memorando_corpo_circular')
    usermoc = UserMoc.objects.get(user=memorandocircular.remetente_circular)
    context = {
        'memorandocircular': memorandocircular,
        'memo_numero_atualizado': memo_numero_atualizado,
        'memorando_assunto_circular': memorandocircular.assunto_circular,
        'data_atual': data_numerica,
        'grupo_escolhido': grupo_escolhido,
        'text_content': mark_safe(text_content),
        'grupos': grupos,
        'usermoc': usermoc,
    }
    return render(request, 'generate_pdf_circular.html', context)

@login_required
def generate_pdf_oficio(request, id_criptografado):
    oficio = Oficio.objects.get(id=id_criptografado)
    destinatario = Oficio.objects.get(id=id_criptografado).destinatario_oficio
    memo_numero_atualizado = oficio.gerar_proximo_numero_oficio()
    data_atual = datetime.date.today()
    data_numerica = data_atual.strftime("%d/%m/%y")
    session = SessionStore(request.session.session_key)
    text_content = session.get('memorando_corpo')
    usermoc = UserMoc.objects.get(user=oficio.remetente_oficio)
    context = {
        'oficio': oficio,
        'memo_numero_atualizado': memo_numero_atualizado,
        'oficio_assunto': oficio.assunto_oficio,
        'data_atual': data_numerica,
        'text_content': mark_safe(text_content),
        'destinatario_oficio': oficio.destinatario_oficio,
        'destinatario_copia_oficio': oficio.destinatarios_copia_oficio,
        'usermoc': usermoc,
    }
    return render(request, 'generate_pdf_oficio.html', context)

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
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            erro = form.errors
            
            form_authentication = AuthenticationForm(request)
            if form.is_valid():    
                user = form.save()
                message_success = 'Senha alterada com sucesso!'
                context = {
                    'form': form_authentication,
                    'form_senha': form,
                    'message_success': message_success, 
                    'logado': False,
                    'erro': erro
                }
                return render(request, 'login.html', context)

        else:
            form = PasswordChangeForm(request.user)
            
        try:
            erro
        except:
            erro = False
        
        return render(request, 'login.html', {'logado': True, 'password_change_form': form, 'erros': erro})
    else:
        if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:        
                    login(request, user)
                    return redirect('loginPage')
        else:
            form = AuthenticationForm(request)
        
        # Adicionar o formulário de alteração de senha ao contexto
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
from django.contrib import messages


def geraEBaixaPDF(request, id_criptografado):
    
    # id_criptografado_criptografado = criptografar_id_criptografado(id_criptografado)
    # url_criptografada = quote(id_criptografado_criptografado)
    memorando = Memorando.objects.get(id=id_criptografado)
    data_atual = datetime.date.today()
    data_numerica = data_atual.strftime("%d/%m/%y")
    session = SessionStore(request.session.session_key)
    grupo_escolhido = session.get('grupo_escolhido')
    arquivos = session.get('file_name')
    text_content = session.get('memorando_corpo')
    grupo_escolhido_copia = session.get('grupo_escolhido_copia')
    usermoc = UserMoc.objects.get(user=memorando.remetente)
    groupuser = memorando.remetente.groups.first()
    groupaddress = GroupMoc.objects.get(group=groupuser)
    
    context = {
        'memorando': memorando,
        'memorando_assunto': memorando.assunto,
        'data_atual': data_numerica,
        'grupo_escolhido': grupo_escolhido,
        'text_content': mark_safe(text_content),
        'grupo_escolhido_copia': grupo_escolhido_copia,
        'arquivos': arquivos,
        'usermoc': usermoc,
        'grupomoc': groupaddress,
    }
    
    
    html_path = str(BASE_DIR) + "/memoApp/templates/generate_pdf.html"

    # path_wkhtmltopdf = 'C:\Program Files\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
    output_pdf = str(BASE_DIR)+'\\pdf_criado.pdf'
    html_render = render_to_string('generate_pdf.html', context, request=request)
    
    # config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    pathToPdf = str(BASE_DIR)+'/fileStorage/memorando' + str(id_criptografado) + '.pdf'

    with open(str(BASE_DIR)+'/memoApp/static/css/style.css', 'r') as arquivoCss:
        conteudo = arquivoCss.read()
        
    arrayAttachment = []
    
    for arquivo in arquivos:
        attachmentFile = Attachment(arquivo)
        arrayAttachment.append(attachmentFile)
        print(attachmentFile)
    
    HTML(string=html_render).write_pdf(pathToPdf, stylesheets=[CSS(string=conteudo)], attachments=arrayAttachment)
    
    add_image(arquivos, pathToPdf, output_pdf)
    
    
    with open(output_pdf, 'rb') as f:
            response = HttpResponse(f, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="memorando.pdf"'
            return response
        

def geraEBaixaPDFCircular(request, id_criptografado):
    
    # id_criptografado_criptografado = criptografar_id_criptografado(id_criptografado)
    # url_criptografada = quote(id_criptografado_criptografado)
    grupos = Group.objects.all()
    memorando = Memorando.objects.get(id=id_criptografado)
    memorandocircular = MemorandoCircular.objects.get(id=id_criptografado)
    data_atual = datetime.date.today()
    data_numerica = data_atual.strftime("%d/%m/%y")
    session = SessionStore(request.session.session_key)
    grupo_escolhido = session.get('grupo_escolhido')
    arquivos = session.get('file_name')
    text_content = session.get('memorando_corpo_circular')
    usermoc = UserMoc.objects.get(user=memorandocircular.remetente_circular)
    groupuser = memorandocircular.remetente_circular.groups.first()
    groupaddress = GroupMoc.objects.get(group=groupuser)
    context = {
        'memorando': memorando,
        'memorandocircular': memorandocircular,
        'memorando_assunto_circular': memorandocircular.assunto_circular,
        'data_atual': data_numerica,
        'grupo_escolhido': grupo_escolhido,
        'text_content': mark_safe(text_content),
        'grupos': grupos,
        'arquivos': arquivos,
        'usermoc': usermoc,
        'grupomoc': groupaddress,
    }
    
    
    html_path = str(BASE_DIR) + "/memoApp/templates/generate_pdf_circular.html"

    # path_wkhtmltopdf = 'C:\Program Files\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
    output_pdf = str(BASE_DIR)+'\\pdf_criado.pdf'
    html_render = render_to_string('generate_pdf_circular.html', context, request=request)
    
    # config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    pathToPdf = str(BASE_DIR)+'/fileStorage/memorando_circular' + str(id_criptografado) + '.pdf'

    with open(str(BASE_DIR)+'/memoApp/static/css/style.css', 'r') as arquivoCss:
        conteudo = arquivoCss.read()

    arrayAttachment = []
    
    for arquivo in arquivos:
        attachmentFile = Attachment(arquivo)
        arrayAttachment.append(attachmentFile)
    
    HTML(string=html_render).write_pdf(pathToPdf, stylesheets=[CSS(string=conteudo)])

    print(arquivos)
    add_image(arquivos, pathToPdf, output_pdf)
    
    
    with open(output_pdf, 'rb') as f:
            response = HttpResponse(f, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="memorando_circular.pdf"'
            return response

def geraEBaixaPDFOficio(request, id_criptografado):
    
    # id_criptografado_criptografado = criptografar_id_criptografado(id_criptografado)
    # url_criptografada = quote(id_criptografado_criptografado)
    memorando = Memorando.objects.get(id=id_criptografado)
    oficio = Oficio.objects.get(id=id_criptografado)
    data_atual = datetime.date.today()
    data_numerica = data_atual.strftime("%d/%m/%y")
    session = SessionStore(request.session.session_key)
    text_content = session.get('memorando_corpo')
    arquivos = session.get('file_name')
    usermoc = UserMoc.objects.get(user=oficio.remetente_oficio)
    groupuser = oficio.remetente_oficio.groups.first()
    groupaddress = GroupMoc.objects.get(group=groupuser)
    context = {
        'memorando': memorando,
        'oficio_assunto': oficio.assunto_oficio,
        'destinatario_oficio': oficio.destinatario_oficio,
        'destinatario_copia_oficio': oficio.destinatarios_copia_oficio,
        'data_atual': data_numerica,
        'text_content': mark_safe(text_content),
        'arquivos': arquivos,
        'usermoc': usermoc,
        'grupomoc': groupaddress,
    }
    print(oficio.destinatarios_copia_oficio)
    
    
    html_path = str(BASE_DIR) + "/memoApp/templates/generate_pdf_oficio.html"

    # path_wkhtmltopdf = 'C:\Program Files\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
    output_pdf = str(BASE_DIR)+'\\pdf_criado.pdf'
    html_render = render_to_string('generate_pdf_oficio.html', context, request=request)
    
    # config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    pathToPdf = str(BASE_DIR)+'/fileStorage/oficio' + str(id_criptografado) + '.pdf'

    with open(str(BASE_DIR)+'/memoApp/static/css/style.css', 'r') as arquivoCss:
        conteudo = arquivoCss.read()

    arrayAttachment = []
    
    for arquivo in arquivos:
        attachmentFile = Attachment(arquivo)
        arrayAttachment.append(attachmentFile)
        print(attachmentFile)
    
    HTML(string=html_render).write_pdf(pathToPdf, stylesheets=[CSS(string=conteudo)])

    add_image(arquivos, pathToPdf, output_pdf)
    
    
    with open(output_pdf, 'rb') as f:
            response = HttpResponse(f, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="oficio.pdf"'
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


def add_image(arquivos, infile, outfile):

    from PyPDF2 import PdfWriter, PdfReader
    import io
    
    print(arquivos)
    
    in_pdf_file = infile
    out_pdf_file = outfile
    # arquivos = ['C:/Users/yan.silva/Documents/Projetos/Memorando_PMNF/uploads/perfeito_kSdyBZs.jpg', 'C:/Users/yan.silva/Documents/Projetos/Memorando_PMNF/uploads/phoca_thumb_l_image03_grd_0IJe7lC.png', 'C:/Users/yan.silva/Documents/Projetos/Memorando_PMNF/uploads/fe_ba6jcnr.png']
    
    width_a4_points = 595.276
    height_a4_points = 841.890
 
    packet = io.BytesIO()
    can = canvas.Canvas(packet)
    #can.drawString(10, 100, "Hello world")
    x_start = (width_a4_points) / 2
    y_start = (height_a4_points) / 2
    
    for arquivo in arquivos:
        can.drawImage(arquivo, x_start, y_start, width=600, preserveAspectRatio=True,  mask='auto', anchorAtXY=True)
        can.showPage()
        
    can.save()
    
    # move to the beginning of the StringIO buffer
    packet.seek(0)
 
    new_pdf = PdfReader(packet)
 
    # read the existing PDF
    existing_pdf = PdfReader(open(in_pdf_file, "rb"))
    output = PdfWriter()
    
    for i in range(len(existing_pdf.pages)):
        page = existing_pdf.pages[i]                                                                                                              
        output.add_page(page)
 
    for i in range(len(new_pdf.pages)):
        page = new_pdf.pages[i]                                                                                                              
        output.add_page(page)
 
    outputStream = open(out_pdf_file, "wb")
    output.write(outputStream)
    outputStream.close()

    # document = aspose.Document(infile)
    
    # image_path = 'C:/Users/yan.silva/Documents/Projetos/Memorando_PMNF/uploads/phoca_thumb_l_image03_grd_0IJe7lC.png'
    
    # document.pages.add()
    # document.pages[2].add_image(image_path, aspose.Rectangle(20, 730, 120, 830, True))
    
    # document.save(outfile)
    

@login_required
def error_image(request):
    return render(request, 'erro.html')

@login_required
def consultaMemo(request):
       
    if request.method == 'POST':
        form = SearchForm(request.POST)
        print(form.errors)
        if form.is_valid():
            buscapornum = None
            buscaporAssunto = None
            tipo = form.cleaned_data['tipo_moc']
            numBusca = form.cleaned_data['numBusca']
            termoBusca = form.cleaned_data['termoBusca']
            ano = form.cleaned_data['ano']
            
            print(termoBusca)
            numBuscaComAno = str(numBusca).zfill(3)+"/"+str(ano)
            
            # if tipo == 'Todos':
            #     mostraTodos(request, numBuscaComAno, termoBusca, ano, form)
                
            if tipo == 'Memorando':
                buscapornum = Memorando.objects.filter(memo_numero=numBuscaComAno)
                buscaporAssunto = Memorando.objects.filter(assunto__icontains=termoBusca)
            if tipo == 'Oficio':
                buscapornum = Oficio.objects.filter(memo_numero_oficio=numBuscaComAno)
                buscaporAssunto = Oficio.objects.filter(assunto_oficio__icontains=termoBusca)
            if tipo == 'Circular':
                buscapornum = MemorandoCircular.objects.filter(memo_numero_circular=numBuscaComAno)
                buscaporAssunto = MemorandoCircular.objects.filter(assunto_circular__icontains=termoBusca)
            
            if termoBusca:
                resultadoQuery = sorted(buscapornum.union(buscaporAssunto), key=lambda x: x not in buscapornum)
            elif numBusca:
                resultadoQuery = buscapornum
            else:
                resultadoQuery = sorted(buscapornum.union(buscaporAssunto), key=lambda x: x not in buscapornum)
                
            context = {
                'buscando': True,
                'objectList': resultadoQuery,
                'form': form,
                'tipo': tipo,
                'numBusca': numBusca,
            }
            
    else:
        form = SearchForm()
        context = {'form': form}
        
    return render(request, 'consulta_memo.html', context)
    
    
@login_required
def visualizaMoc(request, id_criptografado, tipo):
    
    if tipo == 'Memorando':
        memorando = Memorando.objects.get(id=id_criptografado)

        usermoc = UserMoc.objects.get(user=memorando.remetente)

        groupUser = memorando.remetente.groups.first()
        
        queryAnexo = Image.objects.filter(idDoc=id_criptografado, tipoDoc='memorando')
        
        groupuser = memorando.remetente.groups.first()
        groupaddress = GroupMoc.objects.get(group=groupuser)
        
        context = {
            'memorando': memorando,
            'memo_numero': memorando.memo_numero,
            'remetente': memorando.remetente,
            'grupo_remetente': groupUser,
            'memorando_assunto': memorando.assunto,
            'data_atual': memorando.data.date(),
            'grupo_escolhido': memorando.destinatario.all(),
            'text_content': mark_safe(memorando.corpo),
            'grupo_escolhido_copia': memorando.destinatarios_copia.all(),
            'tipo': tipo,
            'anexos': queryAnexo,
            'usermoc': usermoc,
            'grupomoc': groupaddress
        }
        return render(request, 'visualiza_moc.html', context)

    if tipo == 'Circular':
        memorando = MemorandoCircular.objects.get(id=id_criptografado)

        usermoc = UserMoc.objects.get(user=memorando.remetente_circular)

        groupUser = memorando.remetente_circular.groups.first()
        
        queryAnexo = Image.objects.filter(idDoc=id_criptografado, tipoDoc='memorando-circular')
        
        groupuser = memorando.remetente_circular.groups.first()
        groupaddress = GroupMoc.objects.get(group=groupuser)
        
        context = {
            'memorando': memorando,
            'memo_numero': memorando.memo_numero_circular,
            'remetente': memorando.remetente_circular,
            'grupo_remetente': groupUser,
            'memorando_assunto': memorando.assunto_circular,
            'data_atual': memorando.data_circular.date(),
            'grupo_escolhido': memorando.destinatario_circular.all(),
            'text_content': mark_safe(memorando.corpo_circular),
            'tipo': tipo,
            'anexos': queryAnexo,
            'usermoc': usermoc,
            'grupomoc': groupaddress,
        }
        return render(request, 'visualiza_moc.html', context)
    
    if tipo == 'Oficio':
        memorando = Oficio.objects.get(id=id_criptografado)

        usermoc = UserMoc.objects.get(user=oficio.remetente_oficio)

        groupUser = memorando.remetente_oficio.groups.first()
        
        queryAnexo = Image.objects.filter(idDoc=id_criptografado, tipoDoc='oficio')
        
        groupuser = memorando.remetente_oficio.groups.first()
        groupaddress = GroupMoc.objects.get(group=groupuser)
        
        context = {
            'memorando': memorando,
            'memo_numero': memorando.memo_numero_oficio,
            'remetente': memorando.remetente_oficio,
            'grupo_remetente': groupUser,
            'memorando_assunto': memorando.assunto_oficio,
            'data_atual': memorando.data_oficio.date(),
            'grupo_escolhido': memorando.destinatario_oficio,
            'text_content': mark_safe(memorando.corpo_oficio),
            'grupo_escolhido_copia': memorando.destinatarios_copia_oficio,
            'tipo': tipo,
            'anexos': queryAnexo,
            'usermoc': usermoc,
            'grupomoc': groupaddress,
        }
        return render(request, 'visualiza_moc.html', context)


@login_required
def geraPdfVisualiza(request, idpdf, tipo):
    # id_criptografado_criptografado = criptografar_id_criptografado(id_criptografado)
    # url_criptografada = quote(id_criptografado_criptografado)
    
    if tipo == "Memorando":
        memorando = Memorando.objects.get(id=idpdf)
        usuario = memorando.remetente
        assunto = memorando.assunto
        destinatario = memorando.destinatario.all()
        destinatario_copia = memorando.destinatarios_copia.all()
        data = memorando.data
        corpo = memorando.corpo
        
    if tipo == "Circular":
        memorando = MemorandoCircular.objects.get(id=idpdf)
        usuario = memorando.remetente_circular
        assunto = memorando.assunto_circular
        destinatario = memorando.destinatario_circular.all()
        destinatario_copia = None
        data = memorando.data_circular
        corpo = memorando.corpo_circular
        
    if tipo == "Oficio":
        memorando = Oficio.objects.get(id=idpdf)
        usuario = memorando.remetente_oficio
        assunto = memorando.assunto_oficio
        destinatario = memorando.destinatario_oficio
        destinatario_copia = memorando.destinatarios_copia_oficio
        data = memorando.data_oficio
        corpo = memorando.corpo_oficio
        
    groupuser = usuario.groups.first()
    groupaddress = GroupMoc.objects.get(group=groupuser)

    arquivos = Image.objects.filter(idDoc=idpdf, tipoDoc=tipo)
    
    context = {
        'memorando': memorando,
        'memorando_assunto': assunto,
        'data_atual': data,
        'grupo_escolhido': destinatario,
        'text_content': corpo,
        'grupo_escolhido_copia': destinatario_copia,
        'arquivos': arquivos,
        'usermoc': usuario,
        'grupomoc': groupaddress,
    }
    
    
    html_path = str(BASE_DIR) + "/memoApp/templates/generate_pdf.html"

    # path_wkhtmltopdf = 'C:\Program Files\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
    output_pdf = str(BASE_DIR)+'\\pdf_criado.pdf'
    
    if tipo == "Memorando":
        html_render = render_to_string('generate_pdf.html', context, request=request)
    if tipo == "Circular":
        html_render = render_to_string('generate_pdf_circular.html', context, request=request)
    if tipo == "Oficio":
        html_render = render_to_string('generate_pdf_oficio.html', context, request=request)
    
    # config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    pathToPdf = str(BASE_DIR)+'/fileStorage/memorando' + str(idpdf) + '.pdf'

    with open(str(BASE_DIR)+'/memoApp/static/css/style.css', 'r') as arquivoCss:
        conteudo = arquivoCss.read()
        
    arrayAttachment = []
    
    for arquivo in arquivos:
        attachmentFile = Attachment(arquivo)
        arrayAttachment.append(attachmentFile)
        print(attachmentFile)
    
    HTML(string=html_render).write_pdf(pathToPdf, stylesheets=[CSS(string=conteudo)], attachments=arrayAttachment)
    
    add_image(arquivos, pathToPdf, output_pdf)
    
    
    with open(output_pdf, 'rb') as f:
            response = HttpResponse(f, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="memorando.pdf"'
            return response