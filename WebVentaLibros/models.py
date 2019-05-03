from django.db import models
from django.db.models import CharField


class libro (models.Model):
    titulo_libro: models.CharField = models.CharField(max_length=50)
    autor_libro = models.CharField(max_length=50)
    eiditorial_libro = models.CharField(max_length=50)
    descripcion_libro = models.TextField(max_length=180)
    precio_libro = models.IntegerField()










