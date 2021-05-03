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

        botao = QPushButton('Reset',self)
        botao.move(50,520)
        botao.resize(700,50)
        botao.clicked.connect(self.botao_click)

        botao1 = QPushButton('- Decrement',self)
        botao1.move(50,470)
        botao1.resize(700,50)
        botao1.clicked.connect(self.botao_click)

        botao2 = QPushButton('+ Increment',self)
        botao2.move(50,420)
        botao2.resize(700,50)
        botao2.clicked.connect(self.botao_click)

        self.label = QLabel(self)
        self.label.setText("")
        self.label.move(280,50)
        self.label.resize(700,50)
        self.label.setStyleSheet('QLabel {font:bold;font-size:20px}')            
        self.carregarJanela()

    def carregarJanela(self):
        self.setGeometry(self.esquerda,self.topo,self.largura,self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    def botao_click(self):
        self.label.setText('')    
  
       
aplicacao = QApplication(sys.argv)
j = Janela()
sys.exit(aplicacao.exec_())