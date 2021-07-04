from django.contrib import admin
from django.urls import path, re_path, include
from . import views
from rest_framework.routers import DefaultRouter
from gestion_stock.views import (
    producto_detail_view, producto_patch
)

router=DefaultRouter()
router.register("Producto",views.ProductoApi, basename="producto")

urlpatterns = [
    path('',include(router.urls)),
    path('stk_get/<str:pk>/', producto_detail_view, name= "producto_detail_view"),
    path('stk_patch/<int:pk>/', producto_patch, name= "producto_patch"),
]