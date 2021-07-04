from django.db import models
from django.utils import timezone
from django.db.models import Sum, Count

# Create your models here.

class Producto(models.Model):
    id_prod = models.IntegerField(primary_key=True)
    nombre_pro = models.CharField(max_length=100)
    precio = models.IntegerField(default=0)
    cantidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_pro    