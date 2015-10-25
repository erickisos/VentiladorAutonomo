__author__ = 'erick'
import glob
import serial
import time


class ArduinoSerial(object):

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
        dato = self.arduSerial.read(string)
        return dato

    def desconectArduino(self):
        self.arduSerial.setDTR(False)
        time.sleep(0.3)
        self.arduSerial.flushInput()
        self.arduSerial.setDTR()
        time.sleep(0.3)
        self.arduSerial.close()

