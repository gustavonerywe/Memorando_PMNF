from django.db import models
from django import forms
from django.contrib.auth.models import User
from tinymce import models as tinymce_models
from django.utils import timezone
from datetime import datetime
# from . import forms

class Image(models.Model):
    file = models.FileField(upload_to='documents/')     
    class Meta:
        app_label = 'memoApp'
        
    
class Memorando(models.Model):
    data = models.DateTimeField(null=True, default=None, blank=False)
    memo_numero = models.CharField(max_length=220)
    remetente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='memorandos_enviados')
    destinatario = models.ManyToManyField(User, related_name='memorandos_recebidos')
    destinatarios_copia = models.ManyToManyField(User, related_name='destinatarios_copia', null=True)
    assunto = models.CharField(max_length=225, blank=True, null=True)
    corpo = tinymce_models.HTMLField(null=True, default='')
    # anexo = models.ForeignKey(forms.ImageForm, on_delete=models.CASCADE, related_name="anexo_recebido", null=True, blank=False)

    def gerar_proximo_numero(self):
        memo_numero = 0
        ultimo_numero = Memorando.objects.last()
        print(ultimo_numero)
        if ultimo_numero:
            numero =  ultimo_numero.memo_numero.split('/')
            memo_numero = int(numero[0]) + 1
        else:
            memo_numero = 1

        data_atual = timezone.now()
        ano_atual = data_atual.year
        response = f'{memo_numero:003d}/{ano_atual}'
        return response

class Oficio(models.Model):
    data_oficio = models.DateTimeField(null=True, default=None, blank=False)
    memo_numero_oficio = models.CharField(max_length=220)
    remetente_oficio = models.ForeignKey(User, on_delete=models.CASCADE, related_name='memorandos_enviados_oficio')
    destinatario_oficio = models.CharField(max_length=225, blank=True, null=True)
    destinatarios_copia_oficio =  models.CharField(max_length=225, blank=True, null=True)
    assunto_oficio = models.CharField(max_length=225, blank=True, null=True)
    corpo_oficio = tinymce_models.HTMLField(null=True, default='')

    def gerar_proximo_numero_oficio(self):
        memo_numero_oficio = 0
        ultimo_numero = Oficio.objects.last()
        print(ultimo_numero)
        if ultimo_numero:
            numero =  ultimo_numero.memo_numero_oficio.split('/')
            memo_numero_oficio = int(numero[0]) + 1
        else:
            memo_numero_oficio = 1

        data_atual = timezone.now()
        ano_atual = data_atual.year
        response = f'{memo_numero_oficio:003d}/{ano_atual}'
        return response

class MemorandoCircular(models.Model):
    data_circular = models.DateTimeField(null=True, default=None, blank=False)
    memo_numero_circular = models.CharField(max_length=220)
    remetente_circular = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, related_name='memorandos_enviados_circular')
    destinatario_circular = models.ManyToManyField(User, related_name='memorandos_recebidos_circular')
    assunto_circular = models.CharField(max_length=225, blank=True, null=True)
    corpo_circular = tinymce_models.HTMLField(null=True, default='')

    def gerar_proximo_numero_circular(self):
        memo_numero_circular = 0
        ultimo_numero = MemorandoCircular.objects.last()
        print(ultimo_numero)
        if ultimo_numero:
            numero =  ultimo_numero.memo_numero_circular.split('/')
            memo_numero_circular = int(numero[0]) + 1
        else:
            memo_numero_circular = 1

        data_atual = timezone.now()
        ano_atual = data_atual.year
        response = f'{memo_numero_circular:003d}/{ano_atual}'
        return response
