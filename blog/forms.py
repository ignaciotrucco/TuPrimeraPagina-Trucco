from django import forms
from django.utils.timezone import now
from .models import Consultas, Turnos, Pacientes, Medicamentos

class PacientesForm(forms.ModelForm):
    class Meta:
        model = Pacientes
        fields = ["nombre", "edad", "obra_social"]

class TurnosForm(forms.ModelForm):
    class Meta:
        model = Turnos
        fields = ["fecha", "especialidad", "medico_asignado"]
        widgets = {
            "fecha": forms.DateTimeInput(
                attrs={
                    "type": "datetime-local",
                    "min": now().strftime('%Y-%m-%dT%H:%M')
                }
            )
        }

class ConsultasForm(forms.ModelForm):
    class Meta:
        model = Consultas
        fields = ["diagnostico", "receta", "es_urgente"]

class MedicamentosForm(forms.ModelForm):
    class Meta:
        model = Medicamentos
        fields = ["nombre", "laboratorio", "uso_recomendado"]

