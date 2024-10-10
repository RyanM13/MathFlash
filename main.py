from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QLabel, QApplication, QLineEdit
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QIcon
import random

import sys

# Establishing ui
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initui()
        
        
    # Initalize ui
    def initui(self):

        # Setting name of window
        self.setWindowTitle("Calc Memorization")

        # Creating these here for check answer
        self.answers_correct = 0
        self.point_system = 0
        self.miss_counter = 1
        
        # Setting the window Icon
        self.setWindowIcon(QIcon("Icon.ico"))

        # Setting to a grid style layout
        self.layout = QGridLayout() 

        # Resizing window
        self.resize(350,50)
        self.answer_label = QLabel("Answer: ")

        

        title_label = QLabel("Welcome to Calc Memorization!", self)
        title_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        title_label.setAlignment(Qt.AlignTop | Qt.AlignCenter)
        self.layout.addWidget(title_label,0,0,1,2)
        
        Calc_Derivatives = QPushButton("Calc Derivatives", self)
        Calc_Derivatives.clicked.connect(self.SetCalc)
        Calc_Derivatives.setFixedSize(175,30)
        Calc_Derivatives.setToolTip("Learn your Calc Derivatives!")
        self.layout.addWidget(Calc_Derivatives,1,0 )
        
        Trig_Identities = QPushButton("Trig Identities", self)
        Trig_Identities.setToolTip("Learn your trig identities!")
        Trig_Identities.setFixedSize(175,30)
        Trig_Identities.clicked.connect(self.SetTrig)
        self.layout.addWidget(Trig_Identities, 1, 1)
        
        Calc_AntiDerivatives= QPushButton("Calc AntiDerivative", self)
        Calc_AntiDerivatives.setToolTip("Learn your calc AntiDerivatives!")
        Calc_AntiDerivatives.setFixedSize(175,30)
        Calc_AntiDerivatives.clicked.connect(self.SetAntiCalc)
        self.layout.addWidget(Calc_AntiDerivatives,2,0)
        
        title = QPushButton("Title",self)
        title.setFixedSize(175,30)
        title.clicked.connect(self.Title)
        self.layout.addWidget(title, 2, 1)
        
        
        

        
        
        
        self.setLayout(self.layout)

    # Qt didn't like making a new layout in initui so I made a main to call back to instead 
    def Main(self):
       
            self.clear_layout()
            self.resize(350, 50)
            
            title_label = QLabel("Welcome to Calc Memorization!", self)
            title_label.setStyleSheet("font-size: 18px; font-weight: bold;")
            title_label.setAlignment(Qt.AlignTop | Qt.AlignCenter)
            self.layout.addWidget(title_label, 0, 0, 1, 2)
            
           
            
            Calc_Derivatives = QPushButton("Calc Derivatives", self)
            Calc_Derivatives.clicked.connect(self.SetCalc)
            Calc_Derivatives.setFixedSize(175, 30)
            Calc_Derivatives.setToolTip("Learn your Calc Derivatives!")
            self.layout.addWidget(Calc_Derivatives, 1, 0)
            
            Trig_Identities = QPushButton("Trig Identities", self)
            Trig_Identities.setFixedSize(175, 30)
            Trig_Identities.setToolTip("Learn your trig identities!")
            Trig_Identities.clicked.connect(self.SetTrig)
            self.layout.addWidget(Trig_Identities, 1, 1)
            
            Calc_AntiDerivatives = QPushButton("Calc AntiDerivative", self)
            Calc_AntiDerivatives.setFixedSize(175, 30)
            Calc_AntiDerivatives.setToolTip("Learn your calc AntiDerivatives!")
            Calc_AntiDerivatives.clicked.connect(self.SetAntiCalc)
            self.layout.addWidget(Calc_AntiDerivatives, 2, 0)
            
            title = QPushButton("Title",self)
            title.setFixedSize(175,30)
            title.clicked.connect(self.Title)
            self.layout.addWidget(title, 2, 1)
                                  
            
            self.setLayout(self.layout)

        
        
        

    # Title screen just showing my name
    def Title(self):
        self.clear_layout()
        name = QLabel("Made by Ryan Mathews")
        name.setStyleSheet("font-size: 35px; font-weight: bold")
        self.layout.addWidget(name, 0, 0)

    # Setting the title screen to calc 
    def SetCalc(self):
        self.Title_Screen(self.Calc)
        self.lastchoice = None
    # Setting the title screen to trig
    def SetTrig(self):
        self.Title_Screen(self.Trig)
        self.lastchoice = None

    # Setting the title screen to anti calc
    def SetAntiCalc(self):
        self.Title_Screen(self.AntiCalc)
        self.lastchoice = None

    def SetCalcCheck(self):
        self.check_answer(self.calc_answers, self.Calc)

    def SetTrigCheck(self):
        self.check_answer(self.trig_answers, self.Trig)


    # Passing in the correct dict and function
    def SetAntiCalcCheck(self):
        self.check_answer(self.anticalc_answers, self.AntiCalc)

        
   
        
    
    # Derivatives
    def Calc(self):
        self.clear_layout()
        self.calc_answers = {
            "sin x": "cosx",
            "cos x": "-sinx",
            "tan x": "sec^2x",
            "cot x": "-csc^2x",
            "sec x": "secxtanx",
            "csc x": "-cscxcotx",
            "n": "0",
            "x": "1",
            "x^n": "nx^n-1",
            "e^x": "e^x",
            "ln x": "1/x",
            "n^x": "n^xlnx",
            "arcsin": "1/√1-x^2", 
            "arccos x": "-1/√1-x^2",
            "arctanx":  "1/1+x^2", 
            "arc cot x": "-1/1+x^2",
            "arc sec x": "1/x√x^2-1",
            "arc csc x": "-1/x√x^2-1" 
    }

        

        calc_functions = list(self.calc_answers.keys())

        self.random_choice = random.choice(calc_functions)
        while self.random_choice == self.lastchoice:
            self.random_choice = random.choice(calc_functions)   
            
            
        self.lastchoice = self.random_choice
        
        Display_label = QLabel(self.random_choice , self)
        Display_label.setStyleSheet("font-size: 32px; font-weight: bold; color: #333;")
        self.layout.addWidget(Display_label, 0, 0, 1, 4, Qt.AlignCenter)

        # Label for the answer
        answer_label = QLabel("Answer:", self)
        answer_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.layout.addWidget(answer_label, 1, 0, Qt.AlignRight)

        # User answer input
        self.user_answer = QLineEdit(self)
        self.user_answer.setFixedSize(100, 30)  # Increased size for easier input
        self.user_answer.setStyleSheet("font-size: 16px; padding: 5px;")
        self.layout.addWidget(self.user_answer, 1, 1, Qt.AlignLeft)

        # Radical button
        radical_button = QPushButton("√", self)
        radical_button.setFixedSize(50, 30)
        radical_button.clicked.connect(self.radicalsign)
        self.layout.addWidget(radical_button, 1, 2, Qt.AlignLeft)

        back_button = QPushButton("Back", self)
        back_button.setFixedSize(50,30)
        back_button.clicked.connect(self.BackButton)
        self.layout.addWidget(back_button, 0, 0, Qt.AlignRight)
        # Empty stretch to center the elements horizontally
        self.layout.setColumnStretch(0, 1)
        self.layout.setColumnStretch(3, 1)

        # Submit button
        submit_button = QPushButton("Submit", self)
        submit_button.setStyleSheet("font-size: 16px; font-weight: bold; background-color: #4CAF50; color: white; padding: 5px 10px;")
        submit_button.clicked.connect(self.SetCalcCheck)
        self.user_answer.returnPressed.connect(submit_button.click)
        self.layout.addWidget(submit_button, 2, 0, 1, 4, Qt.AlignCenter)

    def BackButton(self):
        self.Main()

        
    # Trig identities  
    def Trig(self):
        self.clear_layout()
        self.trig_answers = {
            "tan θ": "sin θ/cosθ",
            "cot θ": "cos θ/sinθ",
            "cos[π/2 - θ]": "sinθ",
            "sin[π/2 - θ]": "cosθ",
            "cot[π/2 - θ]": "tanθ",
            "tan[π/2 - θ]": "cotθ",
            "sec[π/2 - θ]": "cosecθ",
            "cosec[π/2 - θ]": "secθ",
            "cot θ": "1/tanθ",
            "cosec θ": "1/sinθ",
            "sec θ": "1/cosθ",
            "sin(-θ)": "-sinθ",
            "cos(-θ)": "cosθ",
            "tan(-θ)": "-tanθ",
            "cot(-θ)": "-cotθ",
            "sec(-θ)": "secθ",
            "cosec(-θ)": "-cosecθ",
            "sin^2θ + cos^2θ": "1",
            "1 + tan^2 θ": "sec^2θ", 
            "1 + cot^2 θ": "cosec^2θ", 
            "cos^2θ ": "csc^2θ",
            "1 - sin^2 θ": "cos^2θ",
            "tan^2 θ": "sec^2θ-1",
            "cot^2 θ": "csc^2θ-1",
            "sin^2 θ": "1-cos^2θ",
            "sec^2 θ - tan^2 θ": "1",
            "csc^2 θ - cot^2 θ": "1" 
             
            
        }


        trig_functions = list(self.trig_answers.keys())

        self.random_choice = random.choice(trig_functions)
        while self.random_choice == self.lastchoice:
            self.random_choice = random.choice(trig_functions)   
            
            
        self.lastchoice = self.random_choice
        
        Display_label = QLabel(self.random_choice , self)
        Display_label.setStyleSheet("font-size: 32px; font-weight: bold; color: #333;")
        self.layout.addWidget(Display_label, 0, 0, 1, 4, Qt.AlignCenter)

        # Label for the answer
        answer_label = QLabel("Answer:", self)
        answer_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.layout.addWidget(answer_label, 1, 0, Qt.AlignRight)

        # User answer input
        self.user_answer = QLineEdit(self)
        self.user_answer.setFixedSize(100, 30)  # Increased size for easier input
        self.user_answer.setStyleSheet("font-size: 16px; padding: 5px;")
        self.layout.addWidget(self.user_answer, 1, 1, Qt.AlignLeft)

        # Radical button
        radical_button = QPushButton("√", self)
        radical_button.setFixedSize(50, 30)
        radical_button.clicked.connect(self.radicalsign)
        self.layout.addWidget(radical_button, 1, 2, Qt.AlignLeft)

        # Gives option for theta button
        theta_button = QPushButton("θ", self)
        theta_button.setFixedSize(50,30)
        theta_button.clicked.connect(self.thetasign)
        self.layout.addWidget(theta_button, 1,3, Qt.AlignLeft)
        
        # Back button to go to menu
        back_button = QPushButton("Back", self)
        back_button.setFixedSize(50,30)
        back_button.clicked.connect(self.BackButton)
        back_button.setStyleSheet("margin-right: 20px;")
        self.layout.addWidget(back_button, 0, 0, Qt.AlignRight)

        # Empty stretch to center the elements horizontally
        self.layout.setColumnStretch(0, 1)
        self.layout.setColumnStretch(3, 1)

        # Submit button
        submit_button = QPushButton("Submit", self)
        submit_button.setStyleSheet("font-size: 16px; font-weight: bold; background-color: #4CAF50; color: white; padding: 5px 10px;")
        submit_button.clicked.connect(self.SetTrigCheck)
        self.user_answer.returnPressed.connect(submit_button.click)
        self.layout.addWidget(submit_button, 2, 0, 1, 4, Qt.AlignCenter)

    
    # Antidervatives for calculus 
    def AntiCalc(self):
        self.anticalc_answers = {
            "0": "C",
            "1": "x+C",
            "x^n": "x^n+1/n+1+C",
            "e^x": "e^x+C",
            "1/x": "lnx+C",
            "n^x":
            "n^x/lnn+C",
            "cos x": "sinx+C",
            "sin x": "-cosx+C",
            "sec^2 x": "tanx+C",
            "csc^2 x": "-cotx+C",
            "tan x sec x": "secx+C",
            "cot x csc x": "-cscx+C",
            "1/√1-x^2": "arcsinx+C",
            "-1/√1-x^2": "arccosx+C",
            "1/1+x^2": "arctanx+C", 
            "-1/1+x^2": "arccotx+C",
            "1/x√x^2-1": "arcsecx+C",
            "-1/x√x^2 - 1": "arccscx+C"    
        }
        self.clear_layout()
        
        anticalc_functions = list(self.anticalc_answers.keys())

        self.random_choice = random.choice(anticalc_functions)
        while self.random_choice == self.lastchoice:
            self.random_choice = random.choice(anticalc_functions)   
            
            
        self.lastchoice = self.random_choice
        
        Display_label = QLabel(self.random_choice , self)
        Display_label.setStyleSheet("font-size: 32px; font-weight: bold; color: #333;")
        self.layout.addWidget(Display_label, 0, 0, 1, 4, Qt.AlignCenter)

        # Label for the answer
        answer_label = QLabel("Answer:", self)
        answer_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.layout.addWidget(answer_label, 1, 0, Qt.AlignRight)

        # User answer input
        self.user_answer = QLineEdit(self)
        self.user_answer.setFixedSize(100, 30)  # Increased size for easier input
        self.user_answer.setStyleSheet("font-size: 16px; padding: 5px;")
        self.layout.addWidget(self.user_answer, 1, 1, Qt.AlignLeft)

        # Radical button
        radical_button = QPushButton("√", self)
        radical_button.setFixedSize(50, 30)
        radical_button.clicked.connect(self.radicalsign)
        self.layout.addWidget(radical_button, 1, 2, Qt.AlignLeft)


        back_button = QPushButton("Back", self)
        back_button.setFixedSize(50,30)
        back_button.clicked.connect(self.BackButton)
        self.layout.addWidget(back_button, 0, 0, Qt.AlignRight)
        # Empty stretch to center the elements horizontally
        self.layout.setColumnStretch(0, 1)
        self.layout.setColumnStretch(3, 1)

        # Submit button
        submit_button = QPushButton("Submit", self)
        submit_button.setStyleSheet("font-size: 16px; font-weight: bold; background-color: #4CAF50; color: white; padding: 5px 10px;")
        submit_button.clicked.connect(self.SetAntiCalcCheck)
        self.user_answer.returnPressed.connect(submit_button.click)
        self.layout.addWidget(submit_button, 2, 0, 1, 4, Qt.AlignCenter)
         

    # This is my title screen for each of the modes
    def Title_Screen(self, function):
        self.clear_layout()
        
        back_button = QPushButton("Back", self)
        back_button.setFixedSize(50,30)
        back_button.clicked.connect(self.BackButton)
        self.layout.addWidget(back_button, 0, 0)


        Start_label = QLabel("How to play")
        Start_label.setStyleSheet("font-size: 21px; font-weight: bold")
        Start_label.setAlignment(Qt.AlignTop | Qt.AlignCenter)
        self.layout.addWidget(Start_label, 0,0,1,2)
        
        Text_label = QLabel("To play you have to enter the correct answer to the random problem!")
        Text_label.setStyleSheet("font-size: 15px ")
        Text_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(Text_label, 1, 0, 1, 2)

        start_button = QPushButton("Start!")
        start_button.setStyleSheet("color: green; font-weight: bold")
        self.layout.addWidget(start_button, 2,0, 1, 2)
        start_button.clicked.connect(function)
        
   


    # Appending current text with radical sign
    def radicalsign(self):
        current_text = self.user_answer.text()
        self.user_answer.setText(current_text + "√")


    # Appending current text with theta sign
    def thetasign(self):
        current_text = self.user_answer.text()
        self.user_answer.setText(current_text + "θ")



        

    #clears the layout
    def clear_layout(self):
        #very usefull snippet of code!
        for i in reversed(range(self.layout.count())): 
         self.layout.itemAt(i).widget().setParent(None)


    # All about checking the users answer
    def check_answer(self,answers, function):

        # Need to get a clear window
        self.clear_layout()
        
        back_button = QPushButton("Back", self)
        back_button.setFixedSize(50,30)
        back_button.clicked.connect(self.BackButton)
        self.layout.addWidget(back_button, 0, 0, Qt.AlignRight)
        user_input = self.user_answer.text().strip().lower().replace(" ", "")
        correct_answer = answers[self.random_choice].strip().lower()

    
        # Getting point system and answers correct     
        if user_input == correct_answer:
            self.answers_correct += 1
            self.point_system += 100

            Point_label = QLabel(f"Points: {self.point_system}")
            self.layout.addWidget(Point_label, 0,3, Qt.AlignRight)
            correct_display = QLabel("Correct!")
            correct_display.setStyleSheet("font-weight: bold; font-size: 48px; color: green")
            self.layout.addWidget(correct_display, 0,1, Qt.AlignCenter)
            QTimer.singleShot(1000, function)

        # Getting miss count for life system
        elif self.miss_counter < 3:
            wrong_display = QLabel("Incorrect")
            wrong_display.setStyleSheet("font-weight: bold; font-size: 48px; color: red")
            self.layout.addWidget(wrong_display, 0, 1, Qt.AlignCenter)

            correction = QLabel(f"Correct Answer: {correct_answer}")
            correction.setStyleSheet("font-size: 14px; color: green")
            self.layout.addWidget(correction,2,1, Qt.AlignCenter | Qt.AlignBottom)
            
            # Timer to show correct label            
            QTimer.singleShot(3500, function)

            self.miss_counter +=1

        else:
            # Resetting the misscounter to 1 
            self.miss_counter = 1 
            self.point_system = 0
            self.answers_correct = 0
            wrong_display = QLabel("Incorrect")
            wrong_display.setStyleSheet("font-weight: bold; font-size: 48px; color: red")
            self.layout.addWidget(wrong_display, 0, 1, Qt.AlignCenter)
            
            # Provding correct answer for future
            correction = QLabel(f"Correct Answer: {correct_answer}")
            correction.setStyleSheet("font-size: 14px; color: green")
            self.layout.addWidget(correction,2,1, Qt.AlignCenter | Qt.AlignBottom)
            
            retry_button = QPushButton("Retry?")
            retry_button.clicked.connect(function)
            self.layout.addWidget(retry_button, 1, 1, Qt.AlignCenter | Qt.AlignBottom)
            

# Getting window to actually show 
if __name__ == "__main__":
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())


