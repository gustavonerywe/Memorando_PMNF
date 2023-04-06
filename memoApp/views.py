from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

# Define a view que lida com o upload de arquivos
def upload_file(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'upload.html')

# Define a view para a página inicial
def index(request):
    return render(request, 'index.html')



# Create your views here.
