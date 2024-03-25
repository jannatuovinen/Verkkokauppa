from django.db import models

class Tuote(models.Model):
    teksti = models.CharField(max_lenght=200)
    hinta = models.DecimalField(max_digits=12, decimal_places=2)
