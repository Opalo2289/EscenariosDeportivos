from django.shortcuts import render
from rest_framework import viewsets
from principal.serializers import SolicitudSerializer
from principal.models import Solicitud
# Create your views here.

class SolicitudViewSet(viewsets.ModelViewSet):
    serializer_class = SolicitudSerializer
    queryset = Solicitud.objects.all()