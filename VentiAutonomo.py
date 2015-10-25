# -*- coding: utf-8 -*-
from GUI_VentiAutonomo import Ui_MainWindow
from GraphWidgetImpro import Ui_Form
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ImproGraph import DataList
import PyQt4.Qwt5 as Qwt
import sys


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
        self.timer = QTimer()
        self.timer.start(1000)

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