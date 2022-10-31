from http.client import ImproperConnectionState
from django.shortcuts import render
from pydoc import render_doc
from django.shortcuts import render,get_object_or_404,redirect
from gestorapp.forms import *
from gestorapp.models import *


# Create your views here.
def detallePersona(request,id):
    persona = get_object_or_404(Persona,pk=id)
    return render(request,'detallePersona.html',{'persona':persona})

def nuevaPersona(request):
    if request.method == "POST":
        formaPersona = PersonaForm(request.POST)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')
    else:
         formaPersona=PersonaForm
         return render(request,'agregarPersona.html',{'formaPersona':formaPersona})

def editarPersona(request,id):
    persona= get_object_or_404(Persona,pk=id)
    if request.method == 'POST':
        formaPersona= PersonaForm(request.POST,instance=persona)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')
    else:
        formaPersona = PersonaForm(instance=persona)
        return render(request,'editarPersona.html',{'formaPersona':formaPersona})

def eliminarPersona(request,id):
    persona=get_object_or_404(Persona,pk=id)
    if persona:
        persona.delete()
        return redirect('index')


#EMPEIZAN LAS VISTAS DEL CARRO
def detalleCarro(request,id):
    carro = get_object_or_404(Carro,pk=id)
    return render(request,'detalleCarro.html',{'carro':carro})

def nuevoCarro(request):
    if request.method == "POST":
        formaCarro = CarroForm(request.POST)
        if formaCarro.is_valid():
            formaCarro.save()
            return redirect('orden')
    else:
         formaCarro=CarroForm
         return render(request,'agregarCarro.html',{'formaCarro':formaCarro})

def editarCarro(request,id):
    carro= get_object_or_404(Carro,pk=id)
    if request.method == 'POST':
        carroForm= CarroForm(request.POST,instance=carro)
        if carroForm.is_valid():
            carroForm.save()
            return redirect('orden')
    else:
        carroForm = CarroForm(instance=carro)
        return render(request,'editarCarro.html',{'formaCarro':carroForm})

def eliminarCarro(request,id):
    carro=get_object_or_404(Carro,pk=id)
    if carro:
        carro.delete()
        return redirect('orden')

#Agregar Pista
def detallePista(request,id):
    pista = get_object_or_404(Pista,pk=id)
    return render(request,'detallePista.html',{'pista':pista})

def nuevaPista(request):
    if request.method == "POST":
        formaPista = PistaForm(request.POST)
        if formaPista.is_valid():
            formaPista.save()
            return redirect('pista')
    else:
         formaPista=PistaForm()
         return render(request,'agregarPista.html',{'formaPista':formaPista})

def editarPista(request,id):
    pista= get_object_or_404(Pista,pk=id)
    if request.method == 'POST':
        formaPista= PistaForm(request.POST,instance=pista)
        if formaPista.is_valid():
            formaPista.save()
            return redirect('pista')
    else:
        formaPista = PistaForm(instance=pista)
        return render(request,'editarPista.html',{'formaPista':formaPista})

def eliminarPista(request,id):
    pista=get_object_or_404(Pista,pk=id)
    if pista:
        pista.delete()
        return redirect('BienvenidoPista.html')

