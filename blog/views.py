from django.shortcuts import render, redirect
from .models import Pacientes, Turnos, Consultas, Medicamentos
from .forms import PacientesForm, TurnosForm, ConsultasForm, MedicamentosForm

# Create your views here.
def pacientes_view(request):
    search = request.GET.get('search', None)
    
    if search:
        pacientes = Pacientes.objects.filter(nombre__icontains=search)
    else:
        pacientes = Pacientes.objects.all()
    
    return render(request, 'blog/pacientes.html', context={
        'pacientes': pacientes,
    })

def pacientes_create(request):
    if request.method == 'POST':
        form = PacientesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:pacientes')
    else:
        form = PacientesForm()
        
    return render(request, 'blog/pacientes_create.html', context={
        'form': form,
    })

def turnos_view(request):
    search = request.GET.get('search', None)
    
    if search:
        turnos = Turnos.objects.filter(especialidad__icontains=search)
    else:
        turnos = Turnos.objects.all()
    
    return render(request, 'blog/turnos.html', context={
        'turnos': turnos,
    })

def turnos_create(request):
    if request.method == 'POST':
        form = TurnosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:turnos') 
    else:
        form = TurnosForm()
    
    return render(request, 'blog/turnos_create.html', context={
        'form': form,
    })

def consultas_view(request):
    search = request.GET.get('search', None)
    
    if search:
        consultas = Consultas.objects.filter(diagnostico__icontains=search)
    else:
        consultas = Consultas.objects.all()
    
    return render(request, 'blog/consultas.html', context={
        'consultas': consultas,
    })

def consultas_create(request):
    if request.method == 'POST':
        form = ConsultasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:consultas') 
    else:
        form = ConsultasForm()
    
    return render(request, 'blog/consultas_create.html', context={
        'form': form,
    })

def medicamentos_view(request):
    search = request.GET.get('search', None)
    
    if search:
        medicamentos = Medicamentos.objects.filter(nombre__icontains=search)
    else:
        medicamentos = Medicamentos.objects.all()
    
    return render(request, 'blog/medicamentos.html', context={
        'medicamentos': medicamentos,
    })

def medicamentos_create(request):
    if request.method == 'POST':
        form = MedicamentosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:medicamentos') 
    else:
        form = MedicamentosForm()
    
    return render(request, 'blog/medicamentos_create.html', context={
        'form': form,
    })