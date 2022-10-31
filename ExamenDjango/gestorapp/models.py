from django.db import models
#Create your models here.
class Domicilio(models.Model):
    calle=models.CharField(max_length=255)
    no_calle=models.IntegerField()
    pais=models.CharField(max_length=255)
    def __str__(self) -> str:
        return f'Domicilio{self.id}:{self.calle}{self.no_calle}{self.pais}'

class Carro(models.Model):
    tipo=models.CharField(max_length=255)
    modelo=models.CharField(max_length=255)
    motor=models.CharField(max_length=255)
    color=models.CharField(max_length=255)
    origen=models.CharField(max_length=255)
    def __str__(self) -> str:
        return f'carro{self.id}:{self.tipo}{self.modelo}{self.motor}{self.color}{self.origen}'

class Persona(models.Model):
    nombre=models.CharField(max_length=255)
    apellido=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    domicilio=models.ForeignKey(Domicilio,on_delete=models.SET_NULL,null=True)
    pedido=models.ForeignKey(Carro,on_delete=models.SET_NULL,null=True)
    def __str__(self) -> str:
        return f'persona{self.id}:{self.nombre}{self.apellido}{self.email}{self.domicilio}'
        
class Factura(models.Model):
    numFactura=models.CharField(max_length=255)
    costo=models.IntegerField()
    comprador=models.ForeignKey(Persona,on_delete=models.SET_NULL,null=True)
    compra=models.ForeignKey(Carro,on_delete=models.SET_NULL,null=True)
    def __str__(self) -> str:
        return f'carro{self.id}:{self.numFactura}{self.costo}{self.comprador}{self.compra}'

class Pista(models.Model):
    nombrePista=models.CharField(max_length=255)
    largoPista=models.IntegerField()
    paisOrigen=models.CharField(max_length=255)
    
    def __str__(self) -> str:
     return f'pista{self.id}:{self.nombrePista}{self.largoPista}{self.paisOrigen}'

