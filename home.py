from PyQt5.QtWidgets import *
from PyQt5.QtGui import*
from PyQt5.QtCore import*
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 pushButtom"
        self.top=100
        self.left=100
        self.width = 1024
        self.height = 600




        self.setWindowIcon(QIcon("icon.png"))
        #buttom.move(300,200)

        self.InitUI()


    def InitUI(self):
        width = QDesktopWidget().screenGeometry(-1).width()
        self.setWindowTitle(self.title)
        self.setGeometry(self.top,self.left,self.width,self.height)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        lay = QVBoxLayout(self.central_widget)

        self.button = QPushButton('', self)
        ico = QPixmap('home.png')
        self.button.setIconSize(ico.rect().size());
        self.button.setIcon(QIcon(ico))
        self.button.clicked.connect(self.warning)
        lay.addWidget(self.button)
        self.show()

    def warning(self):
        width = QDesktopWidget().screenGeometry(-1).width()
        self.setWindowTitle(self.title)
        self.setGeometry(self.top,self.left,self.width,self.height)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        lay = QVBoxLayout(self.central_widget)
        self.button = QPushButton('', self)
        ico = QPixmap('warning.png')
        self.button.setIconSize(ico.rect().size());
        self.button.setIcon(QIcon(ico))
        self.button.clicked.connect(self.detect_load)
        lay.addWidget(self.button)
        self.show()

    def detect_load(self):
      print('okay')



App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
