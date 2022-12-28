from django.shortcuts import render
from .models import productos
from .serializers import ProductoSerializer
from rest_framework.response import Response

from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.

@api_view(['GET', 'POST'])
def productos_sinpk(request):
    if request.method == 'GET':
        lista_productos = productos.objects.all()
        serie = ProductoSerializer(lista_productos, many=True)
        return Response(serie.data)
    if request.method == 'POST':
        serie = ProductoSerializer(data=request.data)
        if serie.is_valid():
            serie.save()
            return Response(serie.data, status=status.HTTP_201_CREATED)
        return Response(serie.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PATCH', 'DELETE'])
def productos_conpk(request, pk):
    try:
        producto = productos.objects.get(id=pk)
    except productos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serie = ProductoSerializer(producto)
        return Response(serie.data)
    if request.method == 'DELETE':
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'PATCH':
        serie = ProductoSerializer(producto, data=request.data, partial=True)
        if serie.is_valid():
            serie.save()
            return Response(serie.data, status=status.HTTP_201_CREATED)
        return Response(serie.errors, status=status.HTTP_400_BAD_REQUEST)