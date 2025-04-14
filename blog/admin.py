from django.contrib import admin

# Register your models here.
from .models import Pacientes, Consultas, Medicamentos, Turnos

admin.site.register(Pacientes)
admin.site.register(Consultas)
admin.site.register(Medicamentos)
admin.site.register(Turnos)