from django.contrib import admin
from serialApp.models import Inscritos

# Register your models here.

class InscritosAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'telefono', 'institucion', 'estado', 'observacion']

admin.site.register(Inscritos, InscritosAdmin)