from django.db import models

class Proyecto(models.Model):
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    nombre = models.CharField(max_length=50)
    responsable = models.CharField(max_length=50)
    prioridad = models.IntegerField()
