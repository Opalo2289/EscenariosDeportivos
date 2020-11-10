from django.contrib import admin
from principal import models

# Register your models here.

class RegimenAdmin(admin.ModelAdmin):
    list_display=("id","nombre","descripcion")  

class TipoSolicitanteAdmin(admin.ModelAdmin):
    list_display=("id","nombre","descripcion")

class DisciplinaDeportivaAdmin(admin.ModelAdmin):
    list_display=("id","nombre","descripcion")  

class EscenarioDeportivoAdmin(admin.ModelAdmin):
    list_display=("id","nombre","descripcion")  

class ActividadDeportivaAdmin(admin.ModelAdmin):
    list_display=("id","nombre","descripcion")  

class  SolicitudAdmin(admin.ModelAdmin):
    list_display=("id","nombre","tiposolicitante","direccion","barrio","correo","tipoidentificacion","telefono","sexo","discapacidad","adjuntocedula","adjuntorut","escenario","tipoevento","actividaddeportiva","descripcion")      
    
admin.site.register(models.Solicitud, SolicitudAdmin)
admin.site.register(models.Regimen, RegimenAdmin)
admin.site.register(models.TipoSolicitante, TipoSolicitanteAdmin)
admin.site.register(models.DisciplinaDeportiva, DisciplinaDeportivaAdmin)
admin.site.register(models.EscenarioDeportivo, EscenarioDeportivoAdmin)
admin.site.register(models.ActividadDeportiva, ActividadDeportivaAdmin)
