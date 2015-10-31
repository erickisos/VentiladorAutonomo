# -*- coding: utf-8 -*-
from GUI_VentiAutonomo import Ui_MainWindow
from GraphWidget import Ui_Form
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
from Arduino import ArduinoSerial
from SQL import SQL



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
        self.ventanita.radioManual.setChecked(True)

    def enableButtons(self):
        self.ventanita.BtnSpd1.setEnabled(True)
        self.ventanita.BtnSpd2.setEnabled(True)
        self.ventanita.BtnSpd3.setEnabled(True)

    def disableButtons(self):
        self.ventanita.BtnSpd1.setEnabled(False)
        self.ventanita.BtnSpd2.setEnabled(False)
        self.ventanita.BtnSpd3.setEnabled(False)

    def speedOne(self):
        try:
        #        arduino.Write('1')
            print("Velocidad 1")
        except:
            print("Arduino no está conectado")

    def speedTwo(self):
        try:
        #        arduino.Write('1')
            print("Velocidad 2")
        except:
            print("Arduino no está conectado")

    def speedThree(self):
        try:
        #        arduino.Write('1')
            print("Velocidad 3")
        except:
            print("Arduino no está conectado")


class Dialogo(QDialog):

    def __init__(self):
        QDialog.__init__(self)
        self.dia = Ui_Form()
        self.dia.setupUi(self)
        self.connect(self.dia.qwtPlot, SIGNAL('timeout()'), self.dibujar)
        self.timer = QTimer()
        self.timer.start(1000)

    def dibujar(self):
        pass


def main():
    app = QApplication(sys.argv)
    win = Ventana()
    graph = Dialogo()
    graph.connect(win.ventanita.radioAuto, SIGNAL('clicked()'), graph.show)
    graph.connect(win.ventanita.radioManual, SIGNAL('clicked()'), graph.close)
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
