# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GraphWidget.ui'
#
# Created: Sun Oct 25 13:35:51 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.Qwt5 import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(471, 366)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(471, 366))
        Form.setMaximumSize(QtCore.QSize(471, 366))
        self.tablaTemp = QtGui.QTableWidget(Form)
        self.tablaTemp.setGeometry(QtCore.QRect(320, 10, 141, 341))
        self.tablaTemp.setObjectName(_fromUtf8("tablaTemp"))
        self.tablaTemp.setColumnCount(0)
        self.tablaTemp.setRowCount(0)
        self.qwtPlot = QwtPlot(Form)
        self.qwtPlot.setGeometry(QtCore.QRect(10, 9, 291, 341))
        self.qwtPlot.setObjectName(_fromUtf8("qwtPlot"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Temperatura", None))