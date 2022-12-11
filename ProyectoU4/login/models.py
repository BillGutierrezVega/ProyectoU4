from django.db import models

# Create your models here.
class FormProyecto(models.Model):
    foto = models.CharField(max_length=400)
    titulo_proyecto = models.CharField(max_length=200)
    description_proyecto = models.TextField()
    tags = models.CharField(max_length=100)
    url_github = models.URLField(max_length=400)