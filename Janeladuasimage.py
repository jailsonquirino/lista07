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

        botao1 = QPushButton('Carro Colorido!',self)
        botao1.move(50,500)
        botao1.resize(300,50)
        botao1.clicked.connect(self.botao_click)

        botao2 = QPushButton('Carro Negrito!',self)
        botao2.move(450,500)
        botao2.resize(300,50)
        botao2.clicked.connect(self.botao_click)
        
        self.carro = QLabel(self)
        self.carro.move(110,150)
        self.carro.setPixmap(QtGui.QPixmap('imagens/carro1.png'))
        self.carro.resize(600,200)

        self.carro2 = QLabel(self)
        self.carro2.move(450,150)
        self.carro2.setPixmap(QtGui.QPixmap('imagens/carro4.png'))
        self.carro2.resize(600,200)

      
        self.carregarJanela()

    def carregarJanela(self):
        self.setGeometry(self.esquerda,self.topo,self.largura,self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    def botao_click(self):        
        self.carro1 = QtGui.QPixmap('imagens/carro1.png')
        self.carro2 = QtGui.QPixmap('imagens/carro4.png')
      
        
aplicacao = QApplication(sys.argv)
j = Janela()
sys.exit(aplicacao.exec_())