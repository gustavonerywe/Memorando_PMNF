from django.shortcuts import render, redirect,  get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django import forms
from .models import *
from django.http import Http404
from .forms import ImageForm
from django.utils import timezone
import datetime
from bs4 import BeautifulSoup
from rest_framework.decorators import api_view
from rest_framework.response import Response


@login_required
def upload(request):
    memorando = Memorando()
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid(): 
            memorando.assunto = request.POST.get('assunto_memorando')  
            memorando.corpo = request.POST.get('corpo')   
            memo_numero_atualizado = memorando.gerar_proximo_numero()
            soup = BeautifulSoup(memorando.corpo, 'html.parser')
            plain_text = soup.get_text()
            memorando.data = request.POST.get('data')
            destinatarios = request.POST.getlist('destinatario')
            for destinatario_id in destinatarios:
                destinatario = User.objects.get(id=destinatario_id)
                memorando.destinatario.add(destinatario)
            memorando.remetente = request.user
            memorando.memo_numero = memo_numero_atualizado
            memorando.save()
            image = form.save()
            context={
                'image': image,
                'memorando': memorando,
                'memo_numero_atualizado': memo_numero_atualizado,  
                'memorando_corpo': plain_text,
                'memorando_remetente': memorando.remetente,
                'memorando_assunto': memorando.assunto,
            }

            return render(request, 'upload_success.html', context)
    else:
        form = ImageForm()

    context={
        'form': form,
        'memo_numero_atualizado': memorando.gerar_proximo_numero(),
        'memorando_corpo': memorando.corpo,
        }
    return render(request, 'memo_main.html', context)


@login_required
def data_atual(request):
    data = datetime.date.today()
    context ={
        'data': data
    }
    return render(request, 'memo_main.html', context)

@login_required
def file_detail(request, id):
    try:
         image = Image.objects.get(id=id)
         image_size_kb = round(image.file.size/1024)
         image_size_mb = round(image_size_kb/1024, 2)
         timestamp = timezone.now()
    except Image.DoesNotExist:
        raise Http404("Image does not exist")

    context = {'image': image, 'image_size_mb' : image_size_mb, 'timestamp' : timestamp}
    print(image_size_mb)
    return render(request, 'file_detail.html', context)

        

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


# @login_required
# def emAtendimento(request, id):
#     try:
#         atendimento = Atendimento.objects.get(id=id)
#         atendimento.emAtendimento()
#         context={
#         'senha': atendimento,
#         }        
#     except:
#         context={
#         'senha': '',
#         }
#     return render(request, 'em-atendimento.html', context)


# def file_detail(request, pk):
#     image = get_object_or_404(Image, pk=pk)
#     return render(request, 'file_detail.html', {'image': image})

@login_required
def file_list(request):
    files = Image.objects.all()
    return render(request, 'upload_success.html', {'files': files})

# @login_required
# def generate_next_number():
#     ultimo_numero = UltimoNumero.objects.get_or_create(id=1)
    
#     proximo_numero = ultimo_numero.numero + 1
#     ultimo_numero.numero = proximo_numero
#     ultimo_numero.data_atualizacao = timezone.now()
#     ultimo_numero.save()

#     return f"{proximo_numero:0d}/{timezone.now().year}"

# @api_view(['GET'])
# def next_number(request):
#     proximo_numero = generate_next_number()
#     context ={
#         'proximo_numero': proximo_numero
#     }
#     return Response(context)
