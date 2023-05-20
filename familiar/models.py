from django.db import models

# Create your models here.


class Familiar (models.Model):
    nui = models.IntegerField()
    antecedentes_oncologicos = models.TextField()
    ocupacion = models.CharField(max_length=255)
    #competencias
    #estado_civil
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    telefono = models.IntegerField()

    class Meta:
        db_table = 'familiar'