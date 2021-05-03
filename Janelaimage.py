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

        botao = QPushButton(' Click para trocar o carro!',self)
        botao.move(50,520)
        botao.resize(700,50)
        botao.clicked.connect(self.botao_click)       

        self.carro = QLabel(self)
        self.carro.move(300,150)
        self.carro.setPixmap(QtGui.QPixmap('imagens/carro1.png'))
        self.carro.resize(600,200)
      
        self.carregarJanela()

    def carregarJanela(self):
        self.setGeometry(self.esquerda,self.topo,self.largura,self.altura)        
        self.show()

    def botao_click(self):      
        self.carro3 = QtGui.QPixmap('imagens/carro4.png')
        self.carro.setPixmap(self.carro3)
        
         
aplicacao = QApplication(sys.argv)
j = Janela()
sys.exit(aplicacao.exec_())