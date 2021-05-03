import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication, QPushButton
from PyQt5.QtCore import QSize

class Janela (QMainWindow):
    def __init__(self):
        super().__init__()
        self.topo = 100
        self.esquerda = 100
        self.largura = 800
        self.altura = 600
        self.titulo = "Processamento Digital de Imagens"

        botao = QPushButton(' Click aqui!',self)
        botao.move(50,520)
        botao.resize(700,50)
        botao.clicked.connect(self.botao_click)

        self.label = QLabel(self)
        self.label.setText("ADS 3ºP IFTM")
        self.label.move(280,50)
        self.label.resize(400,50)
        self.label.setStyleSheet('QLabel {font:bold;font-size:20px}')            
        self.carregarJanela()

    def carregarJanela(self):
        self.setGeometry(self.esquerda,self.topo,self.largura,self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    def botao_click(self):
        self.label.setText('Jailson Quirino de Paula')    
  
       
aplicacao = QApplication(sys.argv)
j = Janela()
sys.exit(aplicacao.exec_())