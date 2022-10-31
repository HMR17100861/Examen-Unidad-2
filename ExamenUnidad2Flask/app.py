from flask import Flask,request,url_for,render_template,redirect,session,jsonify
from database import db
from flask_migrate import Migrate
from models import juego,accesorios,consolas
from forms import JuegoForm,AccesorioForm,ConsolaForm
from werkzeug.exceptions import abort


app = Flask(__name__)


#CONFIGURACION DE LA BASE DE DATOS 
USER_DB = 'postgres'
PASS_DB = '12345'
URL_DB = 'localhost'
NAME_DB='flask_examen'
FULL_URL= f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)

#CONFIGURACION DE MIGRACION

migrate = Migrate()
migrate.init_app(app,db)

#FORM
app.config["SECRET_KEY"]="una llave muy secreta"


@app.route('/')
def inicio():
    if 'username' in session:
        return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == "POST":
        usuario = request.form["username"]
        session['username']=usuario
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('inicio'))

@app.route('/salir')
def salir():
    return abort(404)

@app.route('/index')
def index():
    juegos = juego.query.all()
    return render_template('index.html',juegos=juegos)


@app.route('/agregar', methods=['GET','POST'])
def agregar():
    game = juego()
    juegoForm = JuegoForm(obj=game)
    if request.method == 'POST':
        if juegoForm.validate_on_submit():
            juegoForm.populate_obj(game)
            #insert
            db.session.add(game)
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('agregar.html',forma=juegoForm)

@app.route('/addAccesorio', methods=['GET','POST'])
def addAccesorio():
    item = accesorios()
    accesorioForm = AccesorioForm(obj=item)
    if request.method == 'POST':
        if accesorioForm.validate_on_submit():
            accesorioForm.populate_obj(item)
            #insert
            db.session.add(item)
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('agregarAccesorio.html',forma=accesorioForm)



@app.route('/addConsola', methods=['GET','POST'])
def addConsola():
    consol = consolas()
    consolaForm = ConsolaForm(obj=consol)
    if request.method == 'POST':
        if consolaForm.validate_on_submit():
            consolaForm.populate_obj(consol)
            #insert
            db.session.add(consol)
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('agregarConsola.html',forma=consolaForm)

# @app.route('/ver/<int:id>')
# def verDetalle(id):
#     game = juego.query.get_or_404(id)
#     return render_template('detalle.html',game=game)


@app.route('/eliminar/<int:id>')
def eliminar(id):
    game = juego.query.get_or_404(id)
    db.session.delete(game)
    db.session.commit()
    return redirect(url_for('inicio'))


@app.route("/showgame",methods=["POST"])
def mostrarJuego():
    info = request.get_json()
    nombre = info ["nombre"]
    categoria = info["categoria"]
    return f'juego {nombre} {categoria}'

