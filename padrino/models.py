from django.db import models

# Create your models here.

class Padrino(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    tipo_persona = models.CharField(max_length=255)
    estrato = models.IntegerField()
    fecha_nacimiento = models.DateField()
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=255)
    correo = models.EmailField()
    tiempo_apadrinando = models.TextField()
    campo = models.CharField(max_length=255)
    class Meta:
        db_table = 'padrino'
    
