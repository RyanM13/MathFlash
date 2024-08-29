from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QLabel, QVBoxLayout, QApplication
from PyQt5.QtQuick import QQuickView
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QUrl

import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initui()
        

    def initui(self):
        self.setWindowTitle("Calc Memorization")
        layout = QGridLayout()

        
        self.title_label = QLabel("Welcome to Calc Memorization!", self)
        layout.addWidget(self.title_label)
        
        self.Calc_Derivatives = QPushButton("Calc Derivatives", self)
        layout.addWidget(self.Calc_Derivatives)
        
        self.Trig_Identities = QPushButton("Trig Identities", self)
        layout.addWidget(self.Trig_Identities)
        

        
        
        self.setLayout(layout)
        
        

if __name__ == "__main__":
        app = QApplication(sys.argv)
        view = QQuickView()
        view.setSource(QUrl("main.qml"))
        view.show
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())


