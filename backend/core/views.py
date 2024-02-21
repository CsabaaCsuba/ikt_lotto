from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes

# Create your views here.

@api_view(('GET',))
def korabbi_sorsolasok(request):
    data = {'count': 'fasz'}
    return Response(data)

def leggyakoribb_szamok(request):
    return Response({'1':1})

def leghasonlobb_szamok(request):
    return Response({'2':2})

def leghoszabb_sorozatok(request):
    return Response({'3':3})

def grafikonok(request):
    return Response({'4':4})

def erdekessegek(request):
    return Response({'5':5})