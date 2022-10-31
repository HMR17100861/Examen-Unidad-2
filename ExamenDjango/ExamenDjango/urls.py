"""ExamenDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import*
from gestorapp.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
     path('', BienvenidoIndex,name='index'),
     path('listado_persona', ListadoPersona,name='persona'),
     path('listado_carro', ListadoCarro,name='carro'),
     path('listado_pista', ListadoPista,name='pista'),  
    path('detalle_persona/<int:id>',detallePersona),
    path('nueva_persona',nuevaPersona),
    path('editar_persona/<int:id>',editarPersona),
    path('eliminar_persona/<int:id>',eliminarPersona),
    path('detalle_carro/<int:id>',detalleCarro),
    path('nuevo_carro',nuevoCarro),
    path('editar_carro/<int:id>',editarCarro),
    path('eliminar_carro/<int:id>',eliminarCarro),
    path('detalle_pista/<int:id>',detallePista),
    path('nueva_pista',nuevaPista),
    path('editar_pista/<int:id>',editarPista),
    path('eliminar_Pista/<int:id>',eliminarPista),
   
]
