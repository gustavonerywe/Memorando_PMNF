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
    
    # def validate_file_size(value):
    #     tamanho_maximo = 50*1024*1024 
    #     if value.size > tamanho_maximo:
    #        raise forms.ValidationError("O arquivo é muito grande. O tamanho máximo permitido é de 50MB.")
    
class UltimoNumero(models.Model):
    numero = models.IntegerField(default=1)
    data_atualizacao = models.DateTimeField(default=timezone.now)