from django.db import models
from django import forms
from django.contrib.auth.models import User
from tinymce import models as tinymce_models
from django.utils import timezone
from datetime import datetime

class Image(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')    
    class Meta:
        app_label = 'memoApp'
    
class Memorando(models.Model):
    data = models.DateTimeField(null=True, default=None, blank=False)
    memo_numero = models.CharField(max_length=220)
    remetente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='memorandos_enviados')
    destinatario = models.ManyToManyField(User, related_name='memorandos_recebidos')
    assunto = models.CharField(max_length=225, blank=True, null=True)
    corpo = tinymce_models.HTMLField(null=True, default='')

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