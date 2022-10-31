class Persona:
    def __init__(self,id = None,nombre = None,correo = None,edad = None) -> None:
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        

    def __str__(self) -> str:
        return f'Id persona: {self.id} nombre: {self.nombre}, edad: {self.edad} correo: {self.correo}'
