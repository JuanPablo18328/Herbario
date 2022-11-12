from django.shortcuts import render

from web.formularios.formularioPlatos import FormularioRegistroPlatos
from web.formularios.formularioEmpleados import FormularioRegistroEmpleados

# Create your views here.

# CADA VISTA ES UNA FUNCION DE PY


def Home(request):
    return render(request, 'index.html')

def Platos(request):

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

            print(datosLimpios)

    return render(request, 'platos.html',diccionarioEnvioDatos)

def Empleados(request):

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

            print(datosLimpiosEmpleado)
    return render(request, 'empleados.html',diccionarioEnvioDatosEmpleados)



