from rest_framework import serializers
from django.db.models import Sum, Avg
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ("id_prod",'nombre_pro','precio','cantidad')