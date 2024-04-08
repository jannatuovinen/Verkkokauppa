from django.contrib import admin
from .models import Tuote


@admin.register(Tuote)
class TuoteAdmin(admin.ModelAdmin):
    list_display = ["nimi", "hinta", "kuva"]
