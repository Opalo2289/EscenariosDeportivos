from django.shortcuts import render
from rest_framework import viewsets
from principal.serializers import SolicitudSerializer
from principal.models import Solicitud
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as do_login
from django.shortcuts import render, redirect


# Create your views here.

class SolicitudViewSet(viewsets.ModelViewSet):
    serializer_class = SolicitudSerializer
    queryset = Solicitud.objects.filter(estado=1)

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