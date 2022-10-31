from app import db

class juego(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nombrejuego= db.Column(db.String(250))
    genero = db.Column(db.String(250))
    
   

    def __str__(self) -> str:
        return(f'ID:{self.id},'
        f'NombreJuego:{self.nombrejuego},'
        f'genero:{self.genero}')

class consolas(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    modelo = db.Column(db.String(250))

    def __str__(self) -> str:
        return(f'ID:{self.id},'
        f'Modelo:{self.modelo}')

class accesorios(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nombreaccesorio = db.Column(db.String(250))
    marca = db.Column(db.String(250))

    def __str__(self) -> str:
        return(f'ID:{self.id},'
        f'NombreAccesorio:{self.nombreaccesorio},'
        f'Marca:{self.marca}')

class refacciones(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    refaccion = db.Column(db.String(250))
    marca = db.Column(db.String(250))

    def __str__(self) -> str:
        return(f'ID:{self.id},'
        f'Refaccion:{self.refaccion},'
        f'Marca:{self.marca}')


class proveedor(db.Model):
     id = db.Column(db.Integer,primary_key=True)
     nombreproveedor = db.Column(db.String(250))

     def __str__(self) -> str:
        return(f'ID:{self.id},'
        f'NombreProveedor:{self.nombreproveedor}')

     
    
    



