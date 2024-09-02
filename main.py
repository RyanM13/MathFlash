from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QLabel, QApplication, QLineEdit
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QIcon, QPixmap
import random

import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initui()
        

    def initui(self):
        self.setWindowTitle("Calc Memorization")
        
        self.miss_counter = 0
        self.point_system = 0
        self.answers_correct = 0

        self.setWindowIcon(QIcon("mathicon1_s97_icon.ico"))
        self.layout = QGridLayout() 
        self.resize(350,50)
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
      
        self.Trig_Identities.setToolTip("Learn your trig identities!")
        self.Trig_Identities.clicked.connect(self.SetTrig)
        self.layout.addWidget(self.Trig_Identities, 1, 1)
        
        self.Calc_AntiDerivatives= QPushButton("Calc AntiDerivative", self)
        self.layout.addWidget(self.Calc_AntiDerivatives,2,0)
        

        
        
        
        self.setLayout(self.layout)

    def Main(self):
        self.clear_layout()
        self.miss_counter = 0
        self.point_system = 0
        self.answers_correct = 0
        self.resize(350, 50)
        self.answer_label = QLabel("Answer: ")

        
        self.title_label = QLabel("Welcome to Calc Memorization!", self)
        self.title_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.title_label.setAlignment(Qt.AlignTop | Qt.AlignCenter)
        self.layout.addWidget(self.title_label,0,0,1,2)
        
        self.Calc_Derivatives = QPushButton("Calc Derivatives", self)
        self.Calc_Derivatives.clicked.connect(self.SetCalc)
        self.Calc_Derivatives.setStyleSheet("color:green")
        self.layout.addWidget(self.Calc_Derivatives,1,0 )
        
        self.Trig_Identities = QPushButton("Trig Identities", self)
        self.layout.addWidget(self.Trig_Identities, 1, 1)
        self.Trig_Identities.setToolTip("Learn your trig identities!")
        self.Trig_Identities.clicked.connect(self.SetTrig)
        
        self.Calc_AntiDerivatives= QPushButton("Calc AntiDerivative", self)
        self.layout.addWidget(self.Calc_AntiDerivatives,2,0)
        
        
        

    def SetCalc(self):
        self.Title_Screen(self.Calc)
        self.lastchoice = None

    def SetTrig(self):
        self.Title_Screen(self.Trig)
        self.lastchoice = None

    def SetCalcCheck(self):
        self.check_answer(self.calc_answers)

    def SetTrigCheck(self):
        self.check_answer(self.trig_answers)
    
    def Calc(self):
        self.clear_layout()
        self.calc_answers = {
            "sin x": "cos x",
            "cos x": "-sin x",
            "tan x": "sec^2 x",
            "cot x": "-csc^2 x",
            "sec x": "sec x tan x",
            "csc x": "-csc x cot x",
            "n": "0",
            "x": "1",
            "x^n": "nx^n-1",
            "e^x": "e^x",
            "ln x": "1/x",
            "n^x": "n^x lnx",
            "arcsin": "1/√1-x^2", 
            "arccos x": "-1/√1-x^2",
            "arctanx":  "1/1+x^2", 
            "arc cot x": "-1/1+x^2",
            "arc sec x": "1/x√x^2 - 1",
            "arc csc x": "-1/x√x^2 - 1" 
    }

        

        self.calc_functions = list(self.calc_answers.keys())

        self.random_choice = random.choice(self.calc_functions)
        while self.random_choice == self.lastchoice:
            self.random_choice = random.choice(self.calc_functions)   
            
            
        self.lastchoice = self.random_choice
        
        self.Display_label = QLabel(self.random_choice , self)
        self.Display_label.setStyleSheet("font-size: 32px; font-weight: bold; color: #333;")
        self.layout.addWidget(self.Display_label, 0, 0, 1, 4, Qt.AlignCenter)

        # Label for the answer
        self.answer_label = QLabel("Answer:", self)
        self.answer_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.layout.addWidget(self.answer_label, 1, 0, Qt.AlignRight)

        # User answer input
        self.user_answer = QLineEdit(self)
        self.user_answer.setFixedSize(100, 30)  # Increased size for easier input
        self.user_answer.setStyleSheet("font-size: 16px; padding: 5px;")
        self.layout.addWidget(self.user_answer, 1, 1, Qt.AlignLeft)

        # Radical button
        self.radical_button = QPushButton("√", self)
        self.radical_button.setFixedSize(50, 30)
        self.radical_button.clicked.connect(self.radicalsign)
        self.layout.addWidget(self.radical_button, 1, 2, Qt.AlignLeft)


        self.back_button = QPushButton("Back", self)
        self.back_button.setFixedSize(50,30)
        self.back_button.clicked.connect(self.BackButton)
        self.layout.addWidget(self.back_button, 0, 0, Qt.AlignRight)
        # Empty stretch to center the elements horizontally
        self.layout.setColumnStretch(0, 1)
        self.layout.setColumnStretch(3, 1)

        # Submit button
        self.submit_button = QPushButton("Submit", self)
        self.submit_button.setStyleSheet("font-size: 16px; font-weight: bold; background-color: #4CAF50; color: white; padding: 5px 10px;")
        self.submit_button.clicked.connect(self.SetCalcCheck)
        self.user_answer.returnPressed.connect(self.submit_button.click)
        self.layout.addWidget(self.submit_button, 2, 0, 1, 4, Qt.AlignCenter)

    def BackButton(self):
        self.clear_layout 
        self.Main()

        
    
    def Trig(self):
        self.clear_layout()
        self.trig_answers = {
            "tan θ": "sin θ/cos θ",
            "cot θ": "cos θ/sin θ",
            "cos[π/2 - θ]": "sin θ",
            "sin[π/2 - θ]": "cos θ",
            "cot[π/2 - θ]": "tan θ",
            "tan[π/2 - θ]": "cot θ",
            "sec[π/2 - θ]": "cosec θ",
            "cosec[π/2 - θ]": "sec θ",
            "cot θ": "1/tan θ",
            "cosec θ": "1/sin θ",
            "sec θ": "1/cos θ",
            "sin(-θ)": "-sin θ",
            "cos(-θ)": "cos θ",
            "tan(-θ)": "-tan θ",
            "cot(-θ)": "-cot θ",
            "sec(-θ)": "sec θ",
            "cosec(-θ)": "-cosec θ",
            "sin^2θ + cos^2θ": "1",
            "1 + tan^2θ": "sec^2θ", 
            "1 + cot^θ": "cosec^2θ", 
             
            
        }


        self.trig_functions = list(self.trig_answers.keys())

        self.random_choice = random.choice(self.trig_functions)
        while self.random_choice == self.lastchoice:
            self.random_choice = random.choice(self.trig_functions)   
            
            
        self.lastchoice = self.random_choice
        
        self.Display_label = QLabel(self.random_choice , self)
        self.Display_label.setStyleSheet("font-size: 32px; font-weight: bold; color: #333;")
        self.layout.addWidget(self.Display_label, 0, 0, 1, 4, Qt.AlignCenter)

        # Label for the answer
        self.answer_label = QLabel("Answer:", self)
        self.answer_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.layout.addWidget(self.answer_label, 1, 0, Qt.AlignRight)

        # User answer input
        self.user_answer = QLineEdit(self)
        self.user_answer.setFixedSize(100, 30)  # Increased size for easier input
        self.user_answer.setStyleSheet("font-size: 16px; padding: 5px;")
        self.layout.addWidget(self.user_answer, 1, 1, Qt.AlignLeft)

        # Radical button
        self.radical_button = QPushButton("√", self)
        self.radical_button.setFixedSize(50, 30)
        self.radical_button.clicked.connect(self.radicalsign)
        self.layout.addWidget(self.radical_button, 1, 2, Qt.AlignLeft)

        self.theta_button = QPushButton("θ", self)
        self.theta_button.setFixedSize(50,30)
        self.theta_button.clicked.connect(self.thetasign)
        self.layout.addWidget(self.theta_button, 1,3, Qt.AlignLeft)

        # Empty stretch to center the elements horizontally
        self.layout.setColumnStretch(0, 1)
        self.layout.setColumnStretch(3, 1)

        # Submit button
        self.submit_button = QPushButton("Submit", self)
        self.submit_button.setStyleSheet("font-size: 16px; font-weight: bold; background-color: #4CAF50; color: white; padding: 5px 10px;")
        self.submit_button.clicked.connect(self.SetTrigCheck)
        self.user_answer.returnPressed.connect(self.submit_button.click)
        self.layout.addWidget(self.submit_button, 2, 0, 1, 4, Qt.AlignCenter)


         

    def Title_Screen(self, function):
        self.clear_layout()
        
        self.back_button = QPushButton("Back", self)
        self.back_button.setFixedSize(50,30)
        self.back_button.clicked.connect(self.BackButton)
        self.layout.addWidget(self.back_button, 0, 0)


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


    def radicalsign(self):
        current_text = self.user_answer.text()
        self.user_answer.setText(current_text + "√")


    def thetasign(self):
        current_text = self.user_answer.text()
        self.user_answer.setText(current_text + "θ")



        

    def clear_layout(self):
        #clears the layout
        #very usefull snippet of code!
        for i in reversed(range(self.layout.count())): 
         self.layout.itemAt(i).widget().setParent(None)

    def check_answer(self,answers):
        self.clear_layout()
        
        self.back_button = QPushButton("Back", self)
        self.back_button.setFixedSize(50,30)
        self.back_button.clicked.connect(self.BackButton)
        self.layout.addWidget(self.back_button, 0, 0, Qt.AlignRight)
        user_input = self.user_answer.text().strip().lower()
        self.correct_answer = answers[self.random_choice].strip().lower()
        
        if user_input == self.correct_answer:
            self.answers_correct += 1
            if self.answers_correct > 5:
                self.point_system *= 2
            else:
                self.point_system += 100

            self.Point_label = QLabel(f"Points: {self.point_system}")
            self.layout.addWidget(self.Point_label, 0,3, Qt.AlignRight)
            self.correct_display = QLabel("Correct!")
            self.correct_display.setStyleSheet("font-weight: bold; font-size: 48px; color: green")
            self.layout.addWidget(self.correct_display, 0,1, Qt.AlignCenter)
            QTimer.singleShot(1000, self.Calc)
        else:
            self.wrong_display = QLabel("Incorrect")
            self.wrong_display.setStyleSheet("font-weight: bold; font-size: 48px; color: red")
            self.layout.addWidget(self.wrong_display, 0, 1, Qt.AlignCenter)

            self.answers_correct = 0
            
          

            self.correction = QLabel(f"Correct Answer: {self.correct_answer}")
            self.correction.setStyleSheet("font-size: 14px; color: green")
            self.layout.addWidget(self.correction,2,1, Qt.AlignCenter | Qt.AlignBottom)
            
            QTimer.singleShot(3500, self.Calc)

            self.miss_counter +=1

            if self.miss_counter == "3": 
                self.retry_button = QPushButton("Retry?")
                self.retry_button.clicked.connect(self.Calc)
                self.layout.addWidget(self.retry_button, 0, 1, Qt.AlignCenter | Qt.AlignBottom)
            


if __name__ == "__main__":
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())


