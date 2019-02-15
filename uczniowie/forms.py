# -*- coding: utf-8 -*-
# quiz-orm/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, HiddenField, FieldList
from wtforms import SelectField, FormField, BooleanField
from wtforms.validators import Required

blad1 = 'To pole jest wymagane'


class KlasaForm(FlaskForm):
    nazwa = 
    rok naboru =
    rok matury = 

class UczenForm(FlaskForm):
    imie = 
    nazwisko = 
    plec = 
    klasa = 






 class OdpForm(FlaskForm):
    id = HiddenField("Odpowiedz id")
    pytanie = HiddenField("Pytanie id")
    odpowiedz = StringField('Odpowiedź:',
                             validators=[Required(message=blad1)],
                             render_kw={'class':'form-control'})
    odpok = BooleanField('Poprawna:')
    
class PytanieForm(FlaskForm):
    pytanie = StringField('Treść pytania:',
                             validators=[Required(message=blad1)],
                             render_kw={'class':'form-control'})
    kategoria = SelectField('Kategoria', coerce=int)
    odpowiedzi = FieldList(FormField(OdpForm), min_entries=3)
