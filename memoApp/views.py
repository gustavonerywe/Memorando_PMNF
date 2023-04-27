from django.shortcuts import render, redirect,  get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from .models import Image
from django.http import Http404
from .forms import ImageForm
from django.utils import timezone
import datetime


@login_required
def upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image=form.save()
            context={
                'image': image
            }
            return render(request, 'upload_success.html', context)
    else:
        form = ImageForm()

    context={
        'form': form
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


def file_list(request):
    files = Image.objects.all()
    return render(request, 'upload_success.html', {'files': files})
