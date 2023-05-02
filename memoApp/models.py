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
    memo_numero = models.IntegerField()
    remetente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='memorandos_enviados')
    destinatario = models.ManyToManyField(User, related_name='memorandos_recebidos')
    assunto = models.CharField(max_length=255, verbose_name='Digite o assunto', null=True, blank=True)
    corpo_memorando = tinymce_models.HTMLField()

    def gerar_proximo_numero(self):
        memo_numero = self.memo_numero
        ultimo_numero = Memorando.objects.filter(memo_numero=memo_numero, data=timezone.now().year).order_by('data').first()
        if ultimo_numero:
            self.memo_numero = ultimo_numero.memo_numero + 1
            numero_formatado = f"{ultimo_numero.memo_numero+1:0d}"
        else:
            self.memo_numero = 1
            numero_formatado = f"{self.memo_numero:0d}"

        data_atual = timezone.now()
        data_formatada =  data_atual.isoformat()
        data_string = str(data_formatada)
        data = datetime.fromisoformat(data_string[:-6])

        return f"{numero_formatado}/{data.year}"



