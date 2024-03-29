from django.db import models
from django.contrib.auth.models import User, Group
from tinymce import models as tinymce_models
from django.utils import timezone

class Image(models.Model):
    idDoc = models.IntegerField(null=True, blank=False)
    tipoDoc = models.CharField(max_length=50, null=True, blank=False)
    file = models.FileField()     
    class Meta:
        app_label = 'memoApp'
        
    
class Memorando(models.Model):
    data = models.DateTimeField(null=True, default=None, blank=False)
    memo_numero = models.CharField(max_length=220)
    remetente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='memorandos_enviados')
    destinatario = models.ManyToManyField(Group, related_name='memorandos_recebidos')
    destinatarios_copia = models.ManyToManyField(Group, related_name='destinatarios_copia', null=True)
    assunto = models.CharField(max_length=1024, blank=True, null=True)
    corpo = tinymce_models.HTMLField(null=True, default='')
    creatorUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator_user', default=1)
    # anexo = models.ManyToManyField(Image, related_name='anexo', null=True, blank=False)
    # anexo = models.ForeignKey(forms.ImageForm, on_delete=models.CASCADE, related_name="anexo_recebido", null=True, blank=False)

    def gerar_proximo_numero(self):
        ultimo_numero = Memorando.objects.last()
        data_atual = timezone.now()
        ano_atual = data_atual.year
        
        if ultimo_numero:
            numero =  ultimo_numero.memo_numero.split('/')
            if int(numero[1]) == ano_atual:
                memo_numero = int(numero[0]) + 1
            else:
                memo_numero = 1
        else:
            memo_numero = 1

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
    creatorUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator_user_oficio', default=1)

    def gerar_proximo_numero_oficio(self):
        memo_numero_oficio = 0
        ultimo_numero = Oficio.objects.last()
        data_atual = timezone.now()
        ano_atual = data_atual.year
        print(ultimo_numero)
        if ultimo_numero:
            numero =  ultimo_numero.memo_numero_oficio.split('/')
            if int(numero[1]) == ano_atual:
                memo_numero_oficio = int(numero[0]) + 1
            else:
                memo_numero_oficio = 1
        else:
            memo_numero_oficio = 1
            
        response = f'{memo_numero_oficio:003d}/{ano_atual}'
        return response

class MemorandoCircular(models.Model):
    data_circular = models.DateTimeField(null=True, default=None, blank=False)
    memo_numero_circular = models.CharField(max_length=220)
    remetente_circular = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, related_name='memorandos_enviados_circular')
    destinatario_circular = models.ManyToManyField(User, related_name='memorandos_recebidos_circular')
    assunto_circular = models.CharField(max_length=225, blank=True, null=True)
    corpo_circular = tinymce_models.HTMLField(null=True, default='')
    creatorUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator_user_circular', default=1)

    def gerar_proximo_numero_circular(self):
        memo_numero_circular = 0
        ultimo_numero = MemorandoCircular.objects.last()
        data_atual = timezone.now()
        ano_atual = data_atual.year
        
        print(ultimo_numero)
        if ultimo_numero:
            numero =  ultimo_numero.memo_numero_circular.split('/')
            if int(numero[1]) == ano_atual:
                memo_numero_circular = int(numero[0]) + 1
            else:
                memo_numero_circular = 1
        else:
            memo_numero_circular = 1


        response = f'{memo_numero_circular:003d}/{ano_atual}'
        return response
    
class UserMoc(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=7)
    acessoTerceiros = models.BooleanField(default=False)

class GroupMoc(models.Model):
    group = models.OneToOneField(Group, on_delete=models.CASCADE)
    endereco = models.CharField(max_length=225, null=True, blank=False)