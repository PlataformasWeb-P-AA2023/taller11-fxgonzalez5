from django.contrib import admin

# Register your models here.
from proyecto.models import Edificio, Departamento

class EdificioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'ciudad', 'tipo')
    search_fields = ('nombre', 'direccion', 'ciudad', 'tipo')

admin.site.register(Edificio, EdificioAdmin)


class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('propietario', 'costo', 'nro_cuartos', 'edificio')
    search_fields = ('propietario', 'costo', 'nro_cuartos')
    raw_id_fields = ('edificio',)

admin.site.register(Departamento, DepartamentoAdmin)
