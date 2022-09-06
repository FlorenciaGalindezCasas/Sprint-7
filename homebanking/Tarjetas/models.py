from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    
class Tarjetas(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=False)    
    numero = models.IntegerField(primary_key=True)
    cvv = models.IntegerField()  # Field name made lowercase.
    fecha_de_otorgamiento = models.DateField(null=True, blank=True)
    fecha_de_vencimiento = models.DateField(null=True, blank=True)
    tipo_de_tarjeta = models.CharField(max_length=30)
    marca_tarjetas = models.CharField(max_length=30, default='VISA')

    class Meta:
        verbose_name = 'Tarjeta'
        verbose_name_plural = 'Tarjetas'