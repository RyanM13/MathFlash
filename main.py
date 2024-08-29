from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QLabel, QApplication, QToolTip
from PyQt5.QtCore import Qt
import random

import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initui()
        

    def initui(self):
        self.setWindowTitle("Calc Memorization")

        layout = QGridLayout() 
        self.resize(350,75)

        
        self.title_label = QLabel("Welcome to Calc Memorization!", self)
        self.title_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.title_label.setAlignment(Qt.AlignTop | Qt.AlignCenter)
        layout.addWidget(self.title_label,0,0,1,2)
        
        self.Calc_Derivatives = QPushButton("Calc Derivatives", self)
        self.Calc_Derivatives.clicked.connect(self.Calc)
        layout.addWidget(self.Calc_Derivatives,1,0 )
        
        self.Trig_Identities = QPushButton("Trig Identities", self)
        layout.addWidget(self.Trig_Identities, 1, 1)
        self.Trig_Identities.setToolTip("Learn your trig identities!")
        
        self.Calc_AntiDerivatives= QPushButton("Calc AntiDerivative", self)
        layout.addWidget(self.Calc_AntiDerivatives,2,0)
        

        
        
        self.setLayout(layout)
        

    
    def Calc(self):
        sin = "cos x"
        cos = "-sin x"
        tan = "sec^2 x"
        cot = "-csc^2 x"
        sec = "sec x tan x"
        csc = "-csc x cot x"
        list = ["sin", "cos", "tan", "cot", "sec", "csc"]

        print(random.choice(list))
         


if __name__ == "__main__":
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())


