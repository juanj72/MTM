from django.db import models
from dream.models import Dream
from padrino.models import Padrino
from familiar.models import Familiar
# Create your models here.


class Estado(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()

class Eps(models.Model):
    nombre = models.CharField(max_length=255)
    telefono = models.IntegerField()
    correo = models.EmailField()

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
    estado = models.ForeignKey(Estado,on_delete=models.SET_NULL,null=True)
    eps = models.ForeignKey(Eps, on_delete=models.SET_NULL,null=True)
    dream = models.ForeignKey(Dream,on_delete=models.SET_NULL,null=True)
    class Meta:
        db_table = 'paciente'


class padrino(models.Model):
    paciente = models.ForeignKey(Paciente,on_delete=models.SET)
    padrino = models.ForeignKey(Padrino,on_delete=models.SET)

class familiar (models.Model):
    paciente = models.ForeignKey(Paciente,on_delete=models.SET)
    familiar =models.ForeignKey(Familiar,on_delete=models.SET)
    
    
