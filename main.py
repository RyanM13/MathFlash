from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QLabel, QApplication, QLineEdit
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QIcon
import random

import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initui()
        

    def initui(self):
        self.setWindowTitle("Calc Memorization")

        self.setWindowIcon(QIcon("mathicon1_s97_icon.ico"))
        self.layout = QGridLayout() 
        self.resize(350,75)
        self.answer_label = QLabel("Answer: ")

        
        self.title_label = QLabel("Welcome to Calc Memorization!", self)
        self.title_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.title_label.setAlignment(Qt.AlignTop | Qt.AlignCenter)
        self.layout.addWidget(self.title_label,0,0,1,2)
        
        self.Calc_Derivatives = QPushButton("Calc Derivatives", self)
        self.Calc_Derivatives.clicked.connect(self.SetCalc)
        self.Calc_Derivatives.setStyleSheet("padding: 5px 10px; color:green")
        self.layout.addWidget(self.Calc_Derivatives,1,0 )
        
        self.Trig_Identities = QPushButton("Trig Identities", self)
        self.layout.addWidget(self.Trig_Identities, 1, 1)
        self.Trig_Identities.setToolTip("Learn your trig identities!")
        self.Trig_Identities.clicked.connect(self.SetTrig)
        
        self.Calc_AntiDerivatives= QPushButton("Calc AntiDerivative", self)
        self.layout.addWidget(self.Calc_AntiDerivatives,2,0)
        

        
        
        
        self.setLayout(self.layout)
        

    def SetCalc(self):
        self.Title_Screen(self.Calc)

    def SetTrig(self):
        self.Title_Screen(self.Trig)
    
    def Calc(self):
        self.clear_layout()
        self.calc_answers = {
            "sin": "cos x",
            "cos": "-sin x",
            "tan": "sec^2 x",
            "cot": "-csc^2 x",
            "sec": "sec x tan x",
            "csc": "-csc x cot x"
    }

        self.calc_functions = list(self.calc_answers.keys())

        self.random_choice = random.choice(self.calc_functions)
        
        self.Display_label = QLabel(self.random_choice, self)
        self.Display_label.setStyleSheet("font-size: 32px; font-weight: bold; color: #333;")
        self.layout.addWidget(self.Display_label, 0, 0, 1, 2, Qt.AlignCenter)

        # Label for the answer
        self.answer_label = QLabel("Answer:", self)
        self.answer_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.layout.addWidget(self.answer_label, 1, 0, Qt.AlignRight)

        # User answer input
        self.user_answer = QLineEdit(self)
        self.user_answer.setFixedSize(100, 30)  # Increased size for easier input
        self.user_answer.setStyleSheet("font-size: 16px; padding: 5px;")
        self.layout.addWidget(self.user_answer, 2, 0, 1, 2, Qt.AlignCenter)

        # Submit button
        self.submit_button = QPushButton("Submit", self)
        self.submit_button.setStyleSheet("font-size: 16px; font-weight: bold; background-color: #4CAF50; color: white; padding: 5px 10px;")
        self.submit_button.clicked.connect(self.check_answer)
        self.layout.addWidget(self.submit_button, 3, 0, 1, 2, Qt.AlignCenter)

        
    
    def Trig(self):
        print("Placeholder")

         

    def Title_Screen(self, function):
        self.clear_layout()
        
        self.tutorial_button = QPushButton("Tutorial")
        self.tutorial_button.setStyleSheet("font-size: 9px")
        self.layout.addWidget(self.tutorial_button, 0,1, Qt.AlignRight)


        self.Start_label = QLabel("How to play")
        self.Start_label.setStyleSheet("font-size: 21px; font-weight: bold")
        self.Start_label.setAlignment(Qt.AlignTop | Qt.AlignCenter)
        self.layout.addWidget(self.Start_label, 0,0,1,2)
        
        self.Text_label = QLabel("To play you have to enter the correct answer to the random problem!")
        self.Text_label.setStyleSheet("font-size: 15px")
        self.Text_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.Text_label, 1, 0, 1, 2)

        self.start_button = QPushButton("Start!")
        self.start_button.setStyleSheet("color: green; font-weight: bold")
        self.layout.addWidget(self.start_button, 2,0, 1, 2)
        self.start_button.clicked.connect(function)
        
        self.tutorial_button = QPushButton("Tutorial")
        self.tutorial_button.setStyleSheet("font-size: 9px")
        self.layout.addWidget(self.tutorial_button, 0,1, Qt.AlignRight)





        

    def clear_layout(self):
        #clears the layout
        #very usefull snippet of code!
        for i in reversed(range(self.layout.count())): 
         self.layout.itemAt(i).widget().setParent(None)

    def check_answer(self):
        self.clear_layout()
        user_input = self.user_answer.text().strip().lower()
        correct_answer = self.calc_answers[self.random_choice].strip().lower()
        
        if user_input == correct_answer:
            self.correct_display = QLabel("Correct!")
            self.correct_display.setStyleSheet("font-weight: bold; font-size: 48px; color: green")
            self.layout.addWidget(self.correct_display, 0,1, Qt.AlignCenter)
            QTimer.singleShot(1000, self.Calc)
        else:
            self.wrong_display = QLabel("Incorrect")
            self.wrong_display.setStyleSheet("font-weight: bold; font-size: 48px; color: red")
            self.layout.addWidget(self.wrong_display, 0, 1, Qt.AlignCenter)
            self.retry_button = QPushButton("Retry?")
            self.retry_button.clicked.connect(self.Calc)
            self.layout.addWidget(self.retry_button, 0, 1, Qt.AlignCenter | Qt.AlignBottom)


if __name__ == "__main__":
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())


