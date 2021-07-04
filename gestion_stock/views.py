from rest_framework import routers, serializers, viewsets, status
from rest_framework.response import Response
from .serializers import ProductoSerializer
from .models import Producto
from rest_framework import filters
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.shortcuts import render
import requests
from django.views.generic import ListView, TemplateView
from django.shortcuts import render
from rest_framework import viewsets
from django.views.generic import ListView, TemplateView
from django.http import HttpResponseRedirect
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
)
class ProductoApi(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

@api_view(['GET'])
def producto_detail_view(request,pk=None):
    if request.method == 'GET':
        producto = Producto.objects.filter(nombre_pro=pk).first()
        if producto == None:
            return Response("No existe producto.")
        else:
            producto_serializer= ProductoSerializer(producto)
            return Response(producto_serializer.data)


@api_view(['PATCH'])
def producto_patch(request, pk):
    producto = Producto.objects.get(id_prod=pk)
    serializer = ProductoSerializer(instance=producto, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return Response(serializer.data)