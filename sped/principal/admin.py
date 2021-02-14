from django.contrib import admin
from principal import models

# Register your models here.

class DiscapacidadAdmin(admin.ModelAdmin):
    list_display=("id","nombre","descripcion")  
class RegimenAdmin(admin.ModelAdmin):
    list_display=("id","nombre","descripcion")  

class TipoSolicitanteAdmin(admin.ModelAdmin):
    list_display=("id","nombre","descripcion")

class DisciplinaDeportivaAdmin(admin.ModelAdmin):
    list_display=("id","nombre","descripcion")  

class EscenarioDeportivoAdmin(admin.ModelAdmin):
    list_display=("id","nombre","descripcion","foto1","foto2")  

class ActividadDeportivaAdmin(admin.ModelAdmin):
    list_display=("id","nombre","descripcion")  

class  SolicitudAdmin(admin.ModelAdmin):
    list_display=("id","nombre","tiposolicitante","direccion","barrio","correo","tipoidentificacion","telefono","sexo","discapacidad","adjuntocedula","adjuntorut","escenario","tipoevento","actividaddeportiva","descripcion","eventodeportivo", "fecha_creacion", "fecha_modificacion", "fecha_vencimiento","estado")

admin.site.register(models.Solicitud, SolicitudAdmin)
admin.site.register(models.Regimen, RegimenAdmin)
admin.site.register(models.TipoSolicitante, TipoSolicitanteAdmin)
admin.site.register(models.DisciplinaDeportiva, DisciplinaDeportivaAdmin)
admin.site.register(models.EscenarioDeportivo, EscenarioDeportivoAdmin)
admin.site.register(models.ActividadDeportiva, ActividadDeportivaAdmin)
admin.site.register(models.Discapacidad, DiscapacidadAdmin)