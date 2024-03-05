from django.contrib import admin
from django.urls import path, include
from .views import korabbi_sorsolasok, leggyakoribb_szamok, leghasonlobb_szamok, leghoszabb_sorozatok, grafikonok, erdekessegek

urlpatterns = [
    path('sorsolasok', korabbi_sorsolasok),
    path('leggyakoribb', leggyakoribb_szamok),
    path('leghasonlobb', leghasonlobb_szamok),
    path('leghoszabb', leghoszabb_sorozatok),
    # path('grafikonok', grafikonok),
    # path('erdekessegek', erdekessegek),
]
