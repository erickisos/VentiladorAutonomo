# -*- coding: utf-8 -*-
from GUI_VentiAutonomo import Ui_MainWindow
from GraphWidgetImpro import Ui_Form
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ImproGraph import DataList
import PyQt4.Qwt5 as Qwt
import sys
import serial
import glob
import time
import sqlite3


class Ventana(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ventanita = Ui_MainWindow()
        self.ventanita.setupUi(self)
        self.connect(self.ventanita.radioManual, SIGNAL('clicked()'), self.enableButtons)
        self.connect(self.ventanita.radioAuto, SIGNAL('clicked()'), self.disableButtons)
        self.timer = QTimer()
        self.connect(self.ventanita.BtnSpd1, SIGNAL('clicked()'), self.speedOne)
        self.connect(self.ventanita.BtnSpd2, SIGNAL('clicked()'), self.speedTwo)
        self.connect(self.ventanita.BtnSpd3, SIGNAL('clicked()'), self.speedThree)

    def enableButtons(self):
        self.ventanita.BtnSpd1.setEnabled(True)
        self.ventanita.BtnSpd2.setEnabled(True)
        self.ventanita.BtnSpd3.setEnabled(True)

    def disableButtons(self):
        self.ventanita.BtnSpd1.setEnabled(False)
        self.ventanita.BtnSpd2.setEnabled(False)
        self.ventanita.BtnSpd3.setEnabled(False)

    def speedOne(self):
        #        arduino.Write('1')
        print("Velocidad 1")

    def speedTwo(self):
        #        arduino.Write('2')
        print("Velocidad 2")

    def speedThree(self):
        #        arduino.Write('3')
        print("Velocidad 3")


class Dialogo(QDialog):

    def __init__(self, a, b):
        QDialog.__init__(self)
        self.dia = Ui_Form()
        self.dia.setupUi(self)
        self.listaTemp = a
        self.listaTime = b
        self.dibujar()

    def dibujar(self):
        plotYeah = self.graphicar(self.listaTime, self.listaTemp)
        self.dia.verticalLayout.addWidget(plotYeah)

    def graphicar(self, listaTime, listaTemp):
        plot = Qwt.QwtPlot()
        plot.setCanvasBackground(QColor("black"))
        plot.setAxisTitle(Qwt.QwtPlot.xBottom, 'tiempo')
        plot.setAxisTitle(Qwt.QwtPlot.yLeft, 'temperatura')
        plot.setAxisScale(Qwt.QwtPlot.xBottom, 0,200)
        plot.setAxisScale(Qwt.QwtPlot.yLeft, 0,45, 5)
        plot.setAxisAutoScale(Qwt.QwtPlot.xBottom)
#        plot.setAxisAutoScale(Qwt.QwtPlot.yLeft)
        curve = Qwt.QwtPlotCurve('')
        curve.setRenderHint(Qwt.QwtPlotItem.RenderAntialiased)
        pen = QPen(QColor("white"))
        pen.setWidth(2)
        curve.setPen(pen)
        curve.attach(plot)
        x = listaTemp
        y = listaTime
        curve.setData(y, x)
        return plot


class Arduino(object):

    def __init__(self):
        self.searchPort = glob.glob('/dev/ttyACM*')
        self.ArduinoPort = str(self.searchPort)
        self.ArduinoPort = self.ArduinoPort[1:-1]
        self.arduSerial = serial.Serial(self.ArduinoPort, 9600, timeout=1)
        self.arduSerial.open()
        self.arduSerial.setDTR(False)
        time.sleep(0.3)
        self.arduSerial.flushInput()
        self.arduSerial.setDTR()
        time.sleep(0.3)
        self.arduSerial.write('B')

    def Write(self, string):
        self.arduSerial.write(string)

    def Read(self, string):
        dato = self.arduSerial.read()
        return dato

    def desconectArduino(self):
        self.arduSerial.setDTR(False)
        time.sleep(0.3)
        self.arduSerial.flushInput()
        self.arduSerial.setDTR()
        time.sleep(0.3)
        self.arduSerial.close()


class SQL(object):
    def __init__(self):
        self.database = sqlite3.connect('temperatura')
        self.cursor = self.database.cursor()

    def dataWrite(self, string):
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


def main():
    app = QApplication(sys.argv)
    win = Ventana()
    datos = DataList()
    a = datos.dataList()
    b = datos.Tiempo()
    graph = Dialogo(a, b)
    graph.connect(win.ventanita.radioAuto, SIGNAL('clicked()'), graph.show)
    graph.connect(win.ventanita.radioManual, SIGNAL('clicked()'), graph.close)
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()