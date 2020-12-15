from rest_framework import serializers
from principal import models

class TipoSolicitanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TipoSolicitante
        fields = "__all__"

class DisciplinaDeportivaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DisciplinaDeportiva
        fields = "__all__"

class EscenarioDeportivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EscenarioDeportivo
        fields = "__all__"

class ActividadDeportivaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ActividadDeportiva
        fields = "__all__"

class DiscapacidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Discapacidad
        fields = "__all__"

class RegimenSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Regimen
        fields = "__all__"

class SolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Solicitud
        fields = "__all__"        