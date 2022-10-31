from time import strptime
from contrato import  Contrato
from Conexion import Conexion
from logger_base import log
from cursor_del_pool import CursorDelPool
import datetime 
class ContratoDao:
    _SELECCIONAR = "SELECT * FROM contrato1"
    _INSERTAR = "INSERT INTO contrato1(no_contrato, costo, fecha_inicio, fecha_fin) VALUES (%s,%s,%s,%s)"
    _ACTUALIZAR = "UPDATE contrato1 SET no_contrato = %s, costo = %s, fecha_inicio = %s,fecha_fin = %s WHERE id_contrato = %s"
    _ELIMINAR = "DELETE FROM contrato1 WHERE id_contrato = %s"

    @classmethod
    def seleccionar(cls):
       with CursorDelPool() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                contratos = []
                for r in registros:
                    contrato = Contrato(r[0],r[1],r[2],r[3],r[4])
                    contratos.append(contrato)
                return contratos

    @classmethod
    def insertar(cls, contrato):
        with CursorDelPool() as cursor:
            valores = (contrato.no_contrato, contrato.costo, contrato.fecha_ini,contrato.fecha_fin)
            cursor.execute(cls._INSERTAR,valores)
            return cursor.rowcount
    
    @classmethod
    def actualizar(cls,contrato):
        with CursorDelPool() as cursor:
            valores =  (contrato.no_contrato, contrato.costo, contrato.fecha_ini, contrato.fecha_fin, contrato.id_contrato)
            cursor.execute(cls._ACTUALIZAR,valores)
            return cursor.rowcount
    
    @classmethod
    def eliminar(cls,contrato):
        with CursorDelPool() as cursor:
            cursor.execute(cls._ELIMINAR, contrato.id_contrato)
            return cursor.rowcount

if __name__ == '__main__':
    #Insertar 
    
    Contrato1 = Contrato(no_contrato="1",costo=23,fecha_ini="2022-01-01", fecha_fin="2022-01-01")
    ContratosInsertados = ContratoDao.insertar(Contrato1)
    log.debug(f'Contratos insertados {ContratosInsertados}')

    Contrato1 = Contrato(no_contrato="2",costo=23,fecha_ini="2022-01-01", fecha_fin="2022-01-01 00:00:00.00")
    ContratosInsertados = ContratoDao.insertar(Contrato1)
    log.debug(f'Contratos insertados {ContratosInsertados}')

    Contrato1 = Contrato(no_contrato="2",costo=23,fecha_ini="2022-01-01 00:00:00.00", fecha_fin="2022-01-01 00:00:00.00")
    ContratosInsertados = ContratoDao.insertar(Contrato1)
    log.debug(f'Contratos insertados {ContratosInsertados}')

    #Actualizar
    Contrato1 = Contrato(no_contrato="5",costo=23,fecha_ini="2022-01-01 00:00:00.00", fecha_fin="2022-01-01 00:00:00.00", id_contrato=3)
    ContratosActualizados = ContratoDao.actualizar(Contrato1)
    log.debug(f'Contratos actualizados {ContratosActualizados}')

    #Eliminar
    Contrato1 = Contrato(id_contrato = '2')
    ContratosEliminados = ContratoDao.eliminar(Contrato1)
    log.debug(f'Contratos eliminados {ContratosEliminados}')
    #ver
    contratos = ContratoDao.seleccionar()
    for c in contratos:
        log.debug(c)