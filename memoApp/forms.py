from .models import Image
from django import forms
from django.db import models
from django.utils import timezone
from django import forms
from django.core.exceptions import ValidationError

MAX_UPLOAD_SIZE = 104857600  # Define o tamanho máximo em bytes (100 MB)

def validate_file_size(value):
    if value.size > MAX_UPLOAD_SIZE:
        raise ValidationError('O tamanho do arquivo excede o limite permitido (100 MB).')


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('file',)

    file = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}), validators=[validate_file_size], required=False)
    
    def clean_file(self):
        file = self.cleaned_data.get('file')
        if file:
            try:
                validate_file_size(file)
            except ValidationError as e:
                self.add_error('file', e.message)
        return file
    
    # def validate_file_size(value):
    #     tamanho_maximo = 50*1024*1024 
    #     if value.size > tamanho_maximo:
    #        raise forms.ValidationError("O arquivo é muito grande. O tamanho máximo permitido é de 50MB.")
    
class UltimoNumero(models.Model):
    numero = models.IntegerField(default=1)
    data_atualizacao = models.DateTimeField(default=timezone.now)