from django.db import models

class Image(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')    
    class Meta:
        app_label = 'memoApp'



# Create your models here.
