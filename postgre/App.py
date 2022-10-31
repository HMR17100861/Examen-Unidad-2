import psycopg2 
conexion = psycopg2.connect(user = "postgres", password = "admin", host = "localhost", port = "5432",database = "tes_db" )

try:    
    cursor  = conexion.cursor()
    sentencia = "SELECT SUM(costo) FROM contrato1 con JOIN contrato_persona cp ON (con.id_contrato = cp.id_contrato) JOIN persona per ON (per.id = cp.id_persona) WHERE per.correo = %s"
    email = input("Ingrese el email: ")
    cursor.execute(sentencia,email)
    resultado = cursor.fetchall()
    print(resultado)
except Exception as e:
    conexion.rollback()
    print(e)
finally:
    conexion.close
