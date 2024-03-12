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

@api_view(('GET',))
def leggyakoribb_szamok(request):
    gyakoriak = lotto_handling.szamok_gyakorisag_szerint()
    print(gyakoriak)
    top3 = sorted(gyakoriak, key=gyakoriak.get, reverse=True)[:3]
    # print(top3)
    kihuzasuk = []
    for i in range(len(top3)):
        kihuzasuk.append(gyakoriak[top3[i]])
    data = {'gyakoriak':top3, 'kihuzasuk':kihuzasuk}
    return Response(data)

@api_view(('GET',))
def leghasonlobb_szamok(request):
    hasonloak = lotto_handling.leghasonlobb_huzasok()
    data = {'hasonloak':hasonloak}
    print(data)
    return Response(data)

@api_view(('GET',))
def leghoszabb_sorozatok(request):
    leghoszabbak = lotto_handling.a3_leghoszabb_sorozatot_tartalmazo_szamsor()
    data = {'leghoszabbak':leghoszabbak}
    return Response(data)

@api_view(('GET',))
def legkisebb_osszegu_szamsorok(request):
    legkisebbek = lotto_handling.a3_legkisebb_osszegu_szamsor()
    data = {'legkisebbek':legkisebbek}
    return Response(data)

@api_view(('GET',))
def grafikonok(request):
    data = {'success':True}
    return Response(data)

@api_view(('GET',))
def erdekessegek(request):
    data = {'success':True}
    return Response(data)