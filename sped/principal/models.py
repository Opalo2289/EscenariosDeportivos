from django.db import models
from enum import Enum

# Create your models here.

class TipoSolicitante(models.Model):
    id=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)
    def __str__(self):
        return (self.nombre) 

class DisciplinaDeportiva(models.Model):
    id=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)
    def __str__(self):
        return (self.nombre) 

class EscenarioDeportivo(models.Model):
    id=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)
    def __str__(self):
        return (self.nombre) 

class ActividadDeportiva(models.Model):
    id=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)
    def __str__(self):
        return (self.nombre) 

class TipoIdentificacion(Enum):
    cc = "CC"
    ti = "TI"
    pa = "PA"

class Sexo(Enum):
    masculino = "Masculino"
    femenino = "Femenino"

class Discapacidad(models.Model):
    id=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)
    def __str__(self):
        return (self.nombre) 

class Regimen(models.Model):
    id=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)
    def __str__(self):
        return (self.nombre) 

class Solicitud(models.Model):
    id=models.AutoField(primary_key=True)
    tiposolicitante = models.ForeignKey(TipoSolicitante, default="", on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    barrio = models.CharField(max_length=30)
    correo = models.CharField(max_length=30)
    tipoidentificacion = models.CharField(max_length=10,blank=False,choices=[((tag.value, tag.value)) for tag in TipoIdentificacion])   
    telefono = models.CharField(max_length=30)
    sexo = models.CharField(max_length=10,blank=False,choices=[((tag.value, tag.value)) for tag in Sexo])   
    discapacidad = models.ForeignKey(Discapacidad, default="", on_delete=models.CASCADE)
    adjuntocedula = models.FileField(upload_to ='uploads/cedula/% Y/% m/% d/') 
    adjuntorut =  models.FileField(upload_to ='uploads/rut/% Y/% m/% d/')   
    escenario =   models.ForeignKey(EscenarioDeportivo, default="", on_delete=models.CASCADE)
    tipoevento =models.ForeignKey(DisciplinaDeportiva, default="", on_delete=models.CASCADE)
    actividaddeportiva =models.ForeignKey(ActividadDeportiva, default="", on_delete=models.CASCADE)
    descripcion =  models.CharField(max_length=30)
    eventodeportivo = models.ForeignKey(Regimen, default="", on_delete=models.CASCADE)
    def __str__(self):
        return (self.nombre) 