from django.db import models

# Create your models here.

class Paciente(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    nui = models.IntegerField()
    fecha_inicio_tratamiento = models.DateField()
    fecha_ingreso = models.DateField()
    seguro_funebre = models.CharField(max_length=255)
    telefono = models.IntegerField()
    correo = models.EmailField()
    direccion_residencia = models.CharField(max_length=255)


class Dream(models.Model):
    tipo = models.CharField(max_length=255)
    nombre = models.CharField(max_length=300)
    
