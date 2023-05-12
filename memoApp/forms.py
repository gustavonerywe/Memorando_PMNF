from .models import Image
from django import forms
from django.db import models
from django.utils import timezone

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('file',)

    file = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}))
    
class UltimoNumero(models.Model):
    numero = models.IntegerField(default=1)
    data_atualizacao = models.DateTimeField(default=timezone.now)