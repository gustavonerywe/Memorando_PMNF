from django.shortcuts import render, redirect,  get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('name', 'file')

    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

def upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            files = Image.objects.all()
            return render(request, 'upload_success.html', {'files': files})
    else:
        form = ImageForm()
    return render(request, 'upload.html', {'form': form})

def file_detail(request, pk):
    image = get_object_or_404(Image, pk=pk)
    return render(request, 'file_detail.html', {'image': image})

def file_list(request):
    files = Image.objects.all()
    return render(request, 'upload_success.html', {'files': files})
