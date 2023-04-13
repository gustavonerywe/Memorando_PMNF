from django.shortcuts import render, redirect,  get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from .models import Image
from django.http import Http404
from .forms import ImageForm

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
    return render(request, 'upload.html', context)

@login_required
def file_detail(request, id):
    try:
        image = Image.objects.get(id=id)
    except Image.DoesNotExist:
        raise Http404("Image does not exist")

    context = {'image': image}

    return render(request, 'file_detail.html', context)

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
