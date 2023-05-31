from django.db import models

# Create your models here.

class Tipo(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()

    def __str__(self):
        return str(self.nombre)



class Dream (models.Model):
    nombre = models.CharField(max_length=255)
    tipo = models.ForeignKey(Tipo,on_delete=models.SET_NULL,null=True)
    class Meta:
        db_table = 'dream'
    def __str__(self):
        return str(self.nombre)

