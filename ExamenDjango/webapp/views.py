from django.shortcuts import render
from gestorapp.models import *



# Create your views here.

def BienvenidoIndex(request):
    return render(request,'index.html')

def ListadoPersona(request):
    persona = Persona.objects.order_by('id')
   
    return render(request, 'ListadoPersona.html',{'persona': persona})

def ListadoCarro(request):
     carro=Carro.objects.order_by('id')
     return render(request, 'ListadoCarro.html',{'carro': carro})


def ListadoPista(request):
    pista=Pista.objects.order_by('id')
    return render(request,'ListadoPista.html',{'pista':pista})