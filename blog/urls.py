from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('pacientes', views.pacientes_view, name='pacientes'),
    path('pacientes/create', views.pacientes_create, name='pacientes_create'),
    path('turnos', views.turnos_view, name='turnos'),
    path('turnos/create', views.turnos_create, name='turnos_create'),
    path('consultas', views.consultas_view, name='consultas'),
    path('consultas/create', views.consultas_create, name='consultas_create'),
    path('medicamentos', views.medicamentos_view, name='medicamentos'),
    path('medicamentos/create', views.medicamentos_create, name='medicamentos_create'),
]