from django.db import models

# Create your models here.
class Pacientes(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    obra_social = models.CharField(max_length=100)

class Turnos(models.Model):
    fecha = models.DateTimeField()
    especialidad = models.CharField(max_length=100)
    medico_asignado = models.CharField(max_length=100)

class Consultas(models.Model):
    diagnostico = models.CharField(max_length=100)
    receta = models.TextField()
    es_urgente = models.BooleanField(default=False)

class Medicamentos(models.Model):
    nombre = models.CharField(max_length=100)
    laboratorio = models.CharField(max_length=100)
    uso_recomendado = models.TextField()