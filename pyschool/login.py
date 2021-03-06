import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from interface.loginWindow import *
from database.database import Database
from pessoa import Pessoa

import homeProfessor
import homeServidor
import homeAdm

database = Database()

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
tela = Ui_login()
tela.setupUi(MainWindow)
database = Database()

def logar():

    email = tela.lineEmail.text()
    senha = tela.lineSenha.text()

    if email == "":
        raise ValueError
    if senha == "":
        raise ValueError

    id, type = database.autenticar(email, senha)

    if id == None:
        raise UserWarning

    if type == "professor":
        MainWindow.close()
        homeProfessor.startHomeProfessor(id)

    elif type == "servidor":
        MainWindow.close()
        homeServidor.startHomeServidor(id)

    elif type == "administrador":
        MainWindow.close()
        homeAdm.startHomeAdm(id)


def logarCheck():

    try:
        logar()
    
    except UserWarning:
        msg = QMessageBox(None)
        msg.setWindowTitle("Erro")
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Email ou senha incorretos. Por favor, tente novamente.")
        msg.exec_()
        msg.show()


    except ValueError:
        msg = QMessageBox(None)
        msg.setWindowTitle("Erro")
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Por favor, preencha todos os campos.")
        msg.exec_()
        msg.show()


def startLogin():
    tela.btnEntrar.clicked.connect(logarCheck)

    MainWindow.show()


