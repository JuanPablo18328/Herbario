from django.shortcuts import render

from web.formularios.formularioPlatos import FormularioRegistroPlatos
from web.formularios.formularioEmpleados import FormularioRegistroEmpleados
from web.models import Platos, Empleados
# Create your views here.

# CADA VISTA ES UNA FUNCION DE PY


def Home(request):
    return render(request, 'index.html')

def PlatosVista(request):

    #cargar formulario de registro de platos
    formulario = FormularioRegistroPlatos()

    #creamos un diccionario para enviar datos hacia el template
    diccionarioEnvioDatos = {
        'formulario':formulario
    }

    #recibiendo datos del formulario
    #peticion de tipo POST
    if request.method == 'POST':
        datosFormulario = FormularioRegistroPlatos(request.POST)

        if datosFormulario.is_valid():
            datosLimpios = datosFormulario.cleaned_data

            #ENVIANDO DATOS A MI BASE DE DATOS

            platoNuevo = Platos(
                nombre=datosLimpios["nombrePlato"],
                descripcion=datosLimpios["descripcionPlato"],
                imagen=datosLimpios["imagenPlato"],
                precio=datosLimpios["precioPlato"],
                tipo=datosLimpios["tipoPlato"]
            )
            platoNuevo.save()


    return render(request, 'platos.html',diccionarioEnvioDatos)

def EmpleadosVista(request):

    #cargar formulario de registro de platos
    formulario = FormularioRegistroEmpleados()

    #creamos un diccionario para enviar datos hacia el template
    diccionarioEnvioDatosEmpleados = {
        'formularioEmpleados':formulario
    }

    #recibiendo datos del formulario
    #peticion de tipo POST
    if request.method == 'POST':
        datosFormularioEmpleados = FormularioRegistroEmpleados(request.POST)

        if datosFormularioEmpleados.is_valid():
            datosLimpiosEmpleado = datosFormularioEmpleados.cleaned_data

            empleadoNuevo = Empleados(
                nombre=datosLimpiosEmpleado["nombre"],
                descripcion=datosLimpiosEmpleado["descripcion"],
                imagen_perfil=datosLimpiosEmpleado["imagen_Perfil"],
                tipo_documento=datosLimpiosEmpleado["Tipo_Documento"],
                numero_documento=datosLimpiosEmpleado["Numero_Documento"]
            )
            empleadoNuevo.save()

    return render(request, 'empleados.html',diccionarioEnvioDatosEmpleados)



