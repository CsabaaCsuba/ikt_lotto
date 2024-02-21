from django.db import models

# Create your models here.
class Sorsolas(models.Model):
    sorsolasdatum = models.DateField()
    szam1 = models.IntegerField()
    szam2 = models.IntegerField()
    szam3 = models.IntegerField()
    szam4 = models.IntegerField()
    szam5 = models.IntegerField()
