from django.db import models
from enum import Enum

# Create your models here.

class TipoSolicitante(models.Model):
    id=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=60)
    def __str__(self):
        return (self.nombre) 
    class Meta:
        verbose_name = 'Tipo Solicitante'         
        verbose_name_plural = 'Tipos de Solicitante'
class DisciplinaDeportiva(models.Model):
    id=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)
    def __str__(self):
        return (self.nombre) 
    class Meta:
        verbose_name = 'Disciplina Deportiva'         
        verbose_name_plural = 'Disciplinas Deportivas'
class EscenarioDeportivo(models.Model):
    id=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)
    def __str__(self):
        return (self.nombre) 
    class Meta:
        verbose_name = 'Escenario Deportivo'         
        verbose_name_plural = 'Escenarios Deportivos'
class ActividadDeportiva(models.Model):
    id=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)
    def __str__(self):
        return (self.nombre) 
    class Meta:
        verbose_name = 'Actividad Deportiva'         
        verbose_name_plural = 'Actividades Deportivas'
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
    class Meta:
        verbose_name = 'Discapacidad'         
        verbose_name_plural = 'Discapacidades'
class Regimen(models.Model):
    id=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)
    def __str__(self):
        return (self.nombre) 
    class Meta:
        verbose_name = 'Regimen'         
        verbose_name_plural = 'Regímenes'
class Solicitud(models.Model):
    id=models.AutoField(primary_key=True)
    tiposolicitante = models.ForeignKey(TipoSolicitante, default="", on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)
    cedula = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30, null=True, blank = True)
    barrio = models.CharField(max_length=30, null=True, blank = True)
    correo = models.CharField(max_length=30, null=True, blank = True)
    tipoidentificacion = models.CharField(max_length=10,blank=False,choices=[((tag.value, tag.value)) for tag in TipoIdentificacion])   
    telefono = models.CharField(max_length=30, null=True, blank = True)
    sexo = models.CharField(max_length=10, null=True, blank = True,choices=[((tag.value, tag.value)) for tag in Sexo])   
    discapacidad = models.ForeignKey(Discapacidad, default="", on_delete=models.CASCADE)
    adjuntocedula = models.FileField(upload_to ='uploads/cedula/%Y/%m/%d/', null=True, blank = True) 
    adjuntorut =  models.FileField(upload_to ='uploads/rut/%Y/%m/%d/', null=True, blank = True)   
    escenario =   models.ForeignKey(EscenarioDeportivo, default="", on_delete=models.CASCADE)
    tipoevento =models.ForeignKey(DisciplinaDeportiva, default="", on_delete=models.CASCADE)
    actividaddeportiva =models.ForeignKey(ActividadDeportiva, default="", on_delete=models.CASCADE)
    descripcion =  models.CharField(max_length=30, null=True, blank = True)
    eventodeportivo = models.ForeignKey(Regimen, default="", on_delete=models.CASCADE)
    fecha_creacion = models.DateField('Fecha de creación',auto_now= False, auto_now_add = True)
    fecha_modificacion = models.DateField('Fecha de creación',auto_now= True, auto_now_add = False)
    fecha_inicio= models.DateTimeField('Fecha de inicio de la reserva',auto_now= False, auto_now_add = False, null=True, blank = True)
    fecha_vencimiento = models.DateTimeField('Fecha de vencimiento de la reserva',auto_now= False, auto_now_add = False, null=True, blank = True)
    estado = models.BooleanField()
    def __str__(self):
        return (self.nombre)
    class Meta:
        verbose_name = 'Solicitud'         
        verbose_name_plural = 'Solicitudes'
