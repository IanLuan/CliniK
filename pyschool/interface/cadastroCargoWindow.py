# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cadastroCargo.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_background(object):
    def setupUi(self, background):
        background.setObjectName("background")
        background.resize(500, 110)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(background.sizePolicy().hasHeightForWidth())
        background.setSizePolicy(sizePolicy)
        background.setMaximumSize(QtCore.QSize(2000, 450))
        background.setStyleSheet("background-color:  rgb(21, 143, 181)\n"
"")
        self.centralwidget = QtWidgets.QWidget(background)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalWidget.setGeometry(QtCore.QRect(0, 0, 500, 110))
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setContentsMargins(15, 0, 15, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineCargo = QtWidgets.QLineEdit(self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineCargo.sizePolicy().hasHeightForWidth())
        self.lineCargo.setSizePolicy(sizePolicy)
        self.lineCargo.setMinimumSize(QtCore.QSize(20, 0))
        self.lineCargo.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineCargo.setFont(font)
        self.lineCargo.setStyleSheet("QLineEdit { \n"
"border: 5px solid white;\n"
"border-radius: 15px;\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.lineCargo.setClearButtonEnabled(True)
        self.lineCargo.setObjectName("lineCargo")
        self.verticalLayout.addWidget(self.lineCargo)
        self.btnCadastrar = QtWidgets.QPushButton(self.verticalWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btnCadastrar.setFont(font)
        self.btnCadastrar.setStyleSheet("border: 2px solid rgb(255, 123, 28);\n"
"border-radius: 15px;\n"
"background-color: rgb(255, 123, 28);\n"
"color: #fff;")
        self.btnCadastrar.setObjectName("btnCadastrar")
        self.verticalLayout.addWidget(self.btnCadastrar)
        background.setCentralWidget(self.centralwidget)

        self.retranslateUi(background)
        QtCore.QMetaObject.connectSlotsByName(background)

    def retranslateUi(self, background):
        _translate = QtCore.QCoreApplication.translate
        background.setWindowTitle(_translate("background", "Cadastrar Cargo"))
        self.lineCargo.setPlaceholderText(_translate("background", "Nome do Cargo"))
        self.btnCadastrar.setText(_translate("background", "Cadastrar"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    background = QtWidgets.QMainWindow()
    ui = Ui_background()
    ui.setupUi(background)
    background.show()
    sys.exit(app.exec_())
