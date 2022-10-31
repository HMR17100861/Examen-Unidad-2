import email
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired


class JuegoForm(FlaskForm):
    nombrejuego=StringField('Nombre',validators=[DataRequired()])
    genero = StringField('Genero')
    enviar = SubmitField('Enviar')

class AccesorioForm(FlaskForm):
    nombreaccesrio=StringField('Nombre',validators=[DataRequired()])
    marca = StringField('Marca')
    enviar = SubmitField('Enviar')

class ConsolaForm(FlaskForm):
    modelo=StringField('Modelo',validators=[DataRequired()])
    enviar = SubmitField('Enviar')

