from Persona import Persona 
from Conexion import Conexion
from logger_base import log
from cursor_del_pool import CursorDelPool

class PersonaDao:
    _SELECCIONAR = "SELECT * FROM persona"
    _INSERTAR = "INSERT INTO persona(nombre, edad, correo) VALUES (%s,%s,%s)"
    _ACTUALIZAR = "UPDATE persona SET nombre = %s, correo = %s, edad = %s WHERE id = %s"
    _ELIMINAR = "DELETE FROM persona WHERE id = %s"

    @classmethod
    def seleccionar(cls):
       with CursorDelPool() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                personas = []
                for r in registros:
                    persona = Persona(r[0],r[1],r[2],r[3])
                    personas.append(persona)
                return personas

    @classmethod
    def insertar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.nombre, persona.edad, persona.correo)
            cursor.execute(cls._INSERTAR,valores)
            return cursor.rowcount
    
    @classmethod
    def actualizar(cls,persona):
        with CursorDelPool() as cursor:
            valores = (persona.nombre, persona.correo,persona.edad, persona.id)
            cursor.execute(cls._ACTUALIZAR,valores)
            return cursor.rowcount
    
    @classmethod
    def eliminar(cls,persona):
        with CursorDelPool() as cursor:
            cursor.execute(cls._ELIMINAR, persona.id)
            return cursor.rowcount

if __name__ == '__main__':
    #Insertar 
    
    Persona1 = Persona(nombre="Lizandro",correo="lizandro@gmail.com", edad=22)
    personasInsertadas = PersonaDao.insertar(Persona1)
    log.debug(f'Personas insertadas {personasInsertadas}')

    Persona1 = Persona(nombre="Humberto",correo="Humberto@gmail.com", edad=23)
    personasInsertadas = PersonaDao.insertar(Persona1)
    log.debug(f'Personas insertadas {personasInsertadas}')
    
    Persona1 = Persona(nombre="Varela",correo="Varela@gmail.com", edad=24)
    personasInsertadas = PersonaDao.insertar(Persona1)
    log.debug(f'Personas insertadas {personasInsertadas}')

    Persona1 = Persona(nombre="nombre",correo="correo@gmail.com", edad=0)
    personasInsertadas = PersonaDao.insertar(Persona1)
    log.debug(f'Personas insertadas {personasInsertadas}')

    #Actualizar
    Persona1 = Persona(nombre="Varela",correo="Varela123123@gmail.com", edad=24, id=2)
    personasActualizadas = PersonaDao.actualizar(Persona1)
    log.debug(f'Personas actualizadas {personasActualizadas}')

    #Eliminar
    Persona1 = Persona(id = '4')
    personasEliminadas = PersonaDao.eliminar(Persona1)
    log.debug(f'Personas eliminadas {personasEliminadas}')
    #ver
    personas = PersonaDao.seleccionar()
    for c in personas:
        log.debug(c)