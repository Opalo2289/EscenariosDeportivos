from django.contrib import admin
from principal import models

# Register your models here.

class SolicitudAdmin(admin.ModelAdmin):
    list_display=("id","nombre")




admin.site.register(models.Solicitud,SolicitudAdmin)