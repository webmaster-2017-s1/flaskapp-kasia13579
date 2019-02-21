#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  modele.py

from peewee import *

baza_plik = 'uczniowie.db'
baza = SqliteDatabase(baza_plik)  # instancja bazy

class BazaModel(Model):
    class Meta:
        database = baza


class Uczen(BazaModel):
    imie = CharField(max_length=18)
    nazwisko = CharField(max_length=18)
    plec = IntegerField()
    id_klasa = ForeignKey(klasa, related_name="uczniowie")


class Klasa(BazaModel):
    klasa = CharField(max_length=2) 
    roknaboru = IntegerField(default=0)
    rokmatury = IntegerField(default=0)


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
