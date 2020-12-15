from django.shortcuts import render
from rest_framework import viewsets
from principal.serializers import TipoSolicitanteSerializer, DisciplinaDeportivaSerializer, EscenarioDeportivoSerializer, ActividadDeportivaSerializer, DiscapacidadSerializer, RegimenSerializer, SolicitudSerializer
from principal.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as do_login
from django.shortcuts import render, redirect
from django.views.generic import View,TemplateView,ListView

# Create your views here.

class SolicitudViewSet(viewsets.ModelViewSet):
    serializer_class = SolicitudSerializer
    queryset = Solicitud.objects.filter(estado=1)
class TipoSolicitanteViewSet(viewsets.ModelViewSet):
    serializer_class = TipoSolicitanteSerializer
    queryset = TipoSolicitante.objects.all()
class DisciplinaDeportivaViewSet(viewsets.ModelViewSet):
    serializer_class = DisciplinaDeportivaSerializer
    queryset = DisciplinaDeportiva.objects.all()
class EscenarioDeportivoViewSet(viewsets.ModelViewSet):
    serializer_class = EscenarioDeportivoSerializer
    queryset = EscenarioDeportivo.objects.all()
class ActividadDeportivaViewSet(viewsets.ModelViewSet):
    serializer_class = ActividadDeportivaSerializer
    queryset = ActividadDeportiva.objects.all()
class DiscapacidadViewSet(viewsets.ModelViewSet):
    serializer_class = DiscapacidadSerializer
    queryset = Discapacidad.objects.all()
class RegimenViewSet(viewsets.ModelViewSet):
    serializer_class = RegimenSerializer
    queryset = Regimen.objects.all()

def register(request):
    # Creamos el formulario de autenticación vacío
    form = UserCreationForm()
    if request.method == "POST":
        print(request.POST)
        # Añadimos los datos recibidos al formulario
        form = UserCreationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            print("form:",form)
            # Creamos la nueva cuenta de usuario
            user = form.save()

            # Si el usuario se crea correctamente 
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/Usuario_registrado/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "register.html", {'form': form})


class ListadoLibrosReservados(ListView):
    model = Solicitud

    def get_queryset(self):
        queryset = self.model.objects.filter(estado = True)
        return queryset