from rest_framework import serializers
from principal import models

class SolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Solicitud
        fields = "__all__"