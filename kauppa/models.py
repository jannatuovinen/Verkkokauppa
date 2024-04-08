from django.db import models
from django.utils.translation import gettext_lazy as _


class Tuote(models.Model):
    nimi = models.CharField(max_length=200)
    hinta = models.DecimalField(max_digits=12, decimal_places=2)
    kuva = models.ImageField

    class Meta:
        verbose_name = _("tuote")
        verbose_name_plural = _("tuotteet")

    def __str__(self):
        return self.nimi