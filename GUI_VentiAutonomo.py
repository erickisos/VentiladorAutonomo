from PyQt4 import QtCore, QtGui

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(201, 97)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(201, 97))
        MainWindow.setMaximumSize(QtCore.QSize(201, 97))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.BtnSpd1 = QtGui.QPushButton(self.centralwidget)
        self.BtnSpd1.setGeometry(QtCore.QRect(110, 10, 85, 23))
        self.BtnSpd1.setObjectName(_fromUtf8("BtnSpd1"))
        self.BtnSpd1.setToolTip("Presiona para cambiar a velocidad 1")
        self.BtnSpd2 = QtGui.QPushButton(self.centralwidget)
        self.BtnSpd2.setGeometry(QtCore.QRect(110, 39, 85, 23))
        self.BtnSpd2.setObjectName(_fromUtf8("BtnSpd2"))
        self.BtnSpd2.setToolTip("Presiona para cambiar a velocidad 2")
        self.BtnSpd3 = QtGui.QPushButton(self.centralwidget)
        self.BtnSpd3.setGeometry(QtCore.QRect(110, 68, 85, 23))
        self.BtnSpd3.setObjectName(_fromUtf8("BtnSpd3"))
        self.BtnSpd3.setToolTip("Presiona para cambiar a velocidad 3")
        self.radioAuto = QtGui.QRadioButton(self.centralwidget)
        self.radioAuto.setGeometry(QtCore.QRect(10, 10, 113, 19))
        self.radioAuto.setObjectName(_fromUtf8("radioAuto"))
        self.radioManual = QtGui.QRadioButton(self.centralwidget)
        self.radioManual.setGeometry(QtCore.QRect(10, 35, 113, 19))
        self.radioManual.setObjectName(_fromUtf8("radioManual"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Control de Ventilador", None))
        self.BtnSpd1.setText(_translate("MainWindow", "1", None))
        self.BtnSpd2.setText(_translate("MainWindow", "2", None))
        self.BtnSpd3.setText(_translate("MainWindow", "3", None))
        self.radioAuto.setText(_translate("MainWindow", "Auto", None))
        self.radioManual.setText(_translate("MainWindow", "Manual", None))

