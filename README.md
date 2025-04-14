# TuPrimeraPagina-Trucco
superusuario: admin
clave: 123

# 🏥 Sistema de Clínica Médica – Proyecto Django

Este es un proyecto web desarrollado en Django utilizando el patrón **MVT**. El objetivo es gestionar información básica de una clínica médica: pacientes, turnos, consultas médicas y medicamentos.

---

## ✅ Funcionalidades Principales

🔹 **Herencia de plantillas HTML:**  
Se usa una plantilla base (`base.html`) desde la cual heredan todas las demás vistas del proyecto.

🔹 **Cuatro modelos en total, sin relaciones entre ellos:**
1. `Paciente`: nombre, edad, obra social  
2. `Turno`: fecha, especialidad, médico asignado  
3. `Consulta`: diagnóstico, receta, **urgente** (booleano)  
4. `Medicamento`: nombre, laboratorio, uso recomendado

🔹 **Formularios de carga individuales para cada modelo**

---

## ▶️ Orden para probar el proyecto

1. **Inicio**  
   - Ingresar a la página principal: `http://localhost:8000/`  
   - Desde el navbar se puede acceder a las distintas secciones: Pacientes, Turnos, Consultas, Medicamentos, Búsqueda.

2. **Cargar Pacientes**  
   - Ir a la seccion pacientes 
   - Completar el formulario y guardar pacientes.

3. **Cargar Turnos**  
   - Ir a la seccion turnos  
   - Ingresar la fecha, especialidad (por ejemplo, “Pediatría”) y médico asignado.

4. **Cargar Consultas**  
   - Ir a la seccion consultas  
   - Cargar un diagnóstico, receta y marcar si es urgente (booleano).

5. **Cargar Medicamentos**  
   - Ir a la seccion medicamentos  
   - Ingresar nombre, laboratorio y para qué se usa.

- En cada vista habrá un input para filtar segun indique el placeholder.

---

## 🗂️ Estructura de Templates

- `templates/base.html` → plantilla base con navbar
- `templates/pacientes/` → paciente_create.html
- `templates/turnos/` → turnos_create.html
- `templates/consultas/` → consultas_create.html
- `templates/medicamentos/` → medicamentos_create.html


