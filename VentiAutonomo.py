# -*- coding: utf-8 -*-

from GUI_VentiAutonomo import Ui_MainWindow
from GraphWidget import Ui_Form
from PyQt4 import QtCore, QtGui
import sys
import serial
import glob
import time


class Ventana(QtGui.QMainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ventanita = Ui_MainWindow()
        self.ventanita.setupUi(self)
        self.connect(self.ventanita.radioManual, QtCore.SIGNAL('clicked()'), self.enableButtons)
        self.connect(self.ventanita.radioAuto, QtCore.SIGNAL('clicked()'), self.disableButtons)
        self.timer = QtCore.QTimer()
        self.connect(self.ventanita.BtnSpd1, QtCore.SIGNAL('clicked()'), self.speedOne)
        self.connect(self.ventanita.BtnSpd2, QtCore.SIGNAL('clicked()'), self.speedTwo)
        self.connect(self.ventanita.BtnSpd3, QtCore.SIGNAL('clicked()'), self.speedThree)

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


class Dialogo(QtGui.QDialog):

    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.dia = Ui_Form()
        self.dia.setupUi(self)

class Arduino(object):

    def __init__(self):
        self.searchPort = glob.glob('/dev/tty.usbmodem*')
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

    def desconectArduino(self):
        self.arduSerial.setDTR(False)
        time.sleep(0.3)
        self.arduSerial.flushInput()
        self.arduSerial.setDTR()
        time.sleep(0.3)
        self.arduSerial.close()

def main():
    app = QtGui.QApplication(sys.argv)
    win = Ventana()
    graph = Dialogo()
#    arduino = Arduino()
    graph.connect(win.ventanita.radioAuto, QtCore.SIGNAL('clicked()'), graph.show)
    graph.connect(win.ventanita.radioManual, QtCore.SIGNAL('clicked()'), graph.close)
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()