import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from calculatorGUI import *
from calculatorProgram import *

#Viet Pham: vhp4

class AppWindow(Ui_Calculator):
    def __init__(self, calculatorWidget):
        Ui_Calculator.__init__(self)
        self.setupUi(calculatorWidget)
        self.num0.clicked.connect(self.buttonPressed)
        self.num1.clicked.connect(self.buttonPressed)
        self.num2.clicked.connect(self.buttonPressed)
        self.num3.clicked.connect(self.buttonPressed)
        self.num4.clicked.connect(self.buttonPressed)
        self.num5.clicked.connect(self.buttonPressed)
        self.num6.clicked.connect(self.buttonPressed)
        self.num7.clicked.connect(self.buttonPressed)
        self.num8.clicked.connect(self.buttonPressed)
        self.num9.clicked.connect(self.buttonPressed)
        self.decimal.clicked.connect(self.decimalPressed)
        self.add.clicked.connect(self.operButtonPressed)
        self.subtract.clicked.connect(self.operButtonPressed)
        self.multiply.clicked.connect(self.operButtonPressed)
        self.divide.clicked.connect(self.operButtonPressed)
        self.exponent.clicked.connect(self.operButtonPressed)
        self.rightpar.clicked.connect(self.operButtonPressed)
        self.leftpar.clicked.connect(self.operButtonPressed)
        self.clear.clicked.connect(self.clearPressed)
        self.equal.clicked.connect(self.equalPressed)
        #creates a switch in order to have the ability to reset the input box after a calculation has been made
        self.justCalculated = False

    #Action for number getting pressed
    def buttonPressed(self):
        #if number is clicked after a calculation has been made, reset the input box
        if self.justCalculated == True:
            self.input.setText("")
            self.justCalculated = False
        button = calculatorWidget.sender()
        newInput = self.input.text() + button.text()
        self.input.setText(newInput)

    #Action for decimal getting pressed
    def decimalPressed(self):
        if self.justCalculated == True:
            self.input.setText("")
            self.justCalculated = False
        self.input.setText(self.input.text()+".")

    #Action for an operator getting pressed
    def operButtonPressed(self):
        if self.justCalculated == True:
            self.justCalculated = False
        operator = calculatorWidget.sender()
        self.input.setText(self.input.text() + operator.text())

    #Action for the clear button being pressed. Clears the input box
    def clearPressed(self):
        justCalculated = False
        self.input.clear()

    #Action to call calculator function and calculates the expression in the input box
    def equalPressed(self):
        answer = calculator(self.input.text())
        self.input.setText(str(answer))
        self.justCalculated = True


if __name__ == '__main__':
    app=QtWidgets.QApplication(sys.argv)
    calculatorWidget=QtWidgets.QDialog()
    w = AppWindow(calculatorWidget)
    calculatorWidget.show()
    sys.exit(app.exec_())