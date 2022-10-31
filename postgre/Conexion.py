from psycopg2 import pool
import psycopg2 as db
import sys
from logger_base import log
class Conexion:

    _DATABASE = 'tes_db'
    _USER = 'postgres'
    _PASSWORD = 'admin'
    _HOST = '127.0.0.1'
    _PORT = '5432'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    _conexion = None
    _cursor = None

    @classmethod
    def ObtenerConexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion = db.connect(database=cls._DATABASE, user=cls._USER, password=cls._PASSWORD, host=cls._HOST)
                print(cls._conexion)
                return cls._conexion
            except db.DatabaseError as e:
               log.debug(f'Error al obtener la conexion: {e}')
               sys.exit()
        else:
            return cls._conexion

    @classmethod
    def ObtenerPool(cls) :
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(
                    cls._MIN_CON,
                    cls._MAX_CON,
                    host=cls._HOST,
                    user=cls._USER,
                    password=cls._PASSWORD,
                    port = cls._PORT,
                    database=cls._DATABASE)
                log.debug(f'Creacion del pool {cls._pool}')

                return cls._pool
            except Exception as e:
                log.error(f'Ocurrio un error en el pool {e}')
        else :
            return cls._pool

    @classmethod
    def ObtenerConexion(cls):
        conexion = cls.ObtenerPool().getconn()
        log.debug(f'Conexion Obtenida {conexion}')
        return conexion
        
    
    @classmethod
    def LiberarConexiones(cls,conexion):
        cls.ObtenerPool().putconn(conexion)  
        log.debug(f'Conexion regresada: {conexion}')

    @classmethod
    def cerrarConexiones(cls):
        cls.ObtenerPool().closeall

if __name__ == '__main__':
    conexion1 = Conexion.ObtenerConexion()
    conexion2 = Conexion.ObtenerConexion()


