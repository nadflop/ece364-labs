
#######################################################
#   Author:     Nur Nadhira Aqilah Binti Mohd Shah
#   email:      mohdshah@purdue.edu
#   ID:         ee364g02
#   Date:       4/3/2019
#######################################################
import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication
from Lab11.calculator import *

class MathConsumer(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MathConsumer, self).__init__(parent)
        self.setupUi(self)

        self.btnCalculate.clicked.connect(self.calculate)

    def calculate(self):
        self.number1 = self.edtNumber1.text()
        self.number2 = self.edtNumber2.text()
        operator = self.cboOperation.itemText(self.cboOperation.currentIndex())
        if operator == '+': #do addition
            try:
                self.result = float(self.number1) + float(self.number2)
                self.edtResult.setText(str(self.result))
            except:
                raise ValueError("number must be a float or an int")
        elif operator == '-': #do subtraction
            try:
                self.result = float(self.number1) - float(self.number2)
                self.edtResult.setText(str(self.result))
            except:
                raise ValueError("number must be a float or an int")
        elif operator == '*': #do multiplication
            try:
                self.result = float(self.number1) * float(self.number2)
                self.edtResult.setText(str(self.result))
            except:
                raise ValueError("number must be a float or an int")
        elif operator == '/': #do division
            try:
                self.result = float(self.number1) / float(self.number2)
                self.edtResult.setText(str(self.result))
            except:
                raise ValueError("number must be a float or an int")
        else:
            pass




if __name__ == "__main__":
     currentApp = QApplication(sys.argv)
     currentForm = MathConsumer()

     currentForm.show()
     currentApp.exec_()
