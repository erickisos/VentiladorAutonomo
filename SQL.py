#!/usr/bin/python
__author__ = 'erick'

import sqlite3


class SQL(object):
    def __init__(self):
        self.database = sqlite3.connect('temperatura')
        self.cursor = self.database.cursor()

    def dataWrite(self, temperatura, hora):
        try:
            self.cursor.execute("INSERT INTO tiempotemperatura (TEMPERATURA, HORA)\
                VALUES (%d, %s)" %(temperatura, hora))
            self.database.commit()
            print("Valor Agregado Correctamente")
        except:
            self.database.rollback()
            print("Error al agregar valores")

    def dataRead(self):
        try:
            self.cursor.execute("SELECT * FROM tiempotemperatura")
            data = self.cursor.fetchall()
            return data
        except:
            print("error en la lectura")

    def dataSave(self):
        pass