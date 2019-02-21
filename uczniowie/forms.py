# -*- coding: utf-8 -*-
# quiz-orm/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, HiddenField, FieldList
from wtforms import SelectField, FormField, BooleanField
from wtforms.validators import Required

blad1 = 'To pole jest wymagane'


class UczenForm(FlaskForm):
    id = HiddenField("")
    imie = StringField("Imię")
    nazwisko = StringField("Nazwisko")


class KlasaForm(FlaskForm):
    id = HiddenField("klasa id")
    klasa = StringField("Numer klasy: ",
                        validators=[Required(message=blad1)])
    rok_naboru = StringField("Rok_naboru")
    rok_matury = StringField("Rok_matury")

