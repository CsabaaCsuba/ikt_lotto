from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
import lotto_handling

lotto_handling.parse_official_link()

# Create your views here.

@api_view(('GET',))
def korabbi_sorsolasok(request):
    nyeroszamok_1_hete = lotto_handling.nyeroszamok_x_hete(1)
    nyeroszamok_2_hete = lotto_handling.nyeroszamok_x_hete(2)
    # data = {'count': 'fasz'}
    data = {'ny1':nyeroszamok_1_hete, 'ny2':nyeroszamok_2_hete}
    return Response(data)

def leggyakoribb_szamok(request):
    gyakoriak = lotto_handling.szamok_gyakorisag_szerint()
    data = {'gyakoriak':gyakoriak}
    return Response(data)

def leghasonlobb_szamok(request):
    hasonloak = lotto_handling.leghasonlobb_huzasok()
    data = {'hasonloak':hasonloak}
    return Response(data)

def leghoszabb_sorozatok(request):
    leghoszabbak = lotto_handling.a3_leghoszabb_sorozatot_tartalmazo_szamsor()
    data = {'leghoszabbak':leghoszabbak}
    return Response(data)

def legkisebb_osszegu_szamsorok(request):
    legkisebbek = lotto_handling.a3_legkisebb_osszegu_szamsor()
    data = {'legkisebbek':legkisebbek}
    return Response(data)

def grafikonok(request):
    return Response({'4':4})

def erdekessegek(request):
    return Response({'5':5})