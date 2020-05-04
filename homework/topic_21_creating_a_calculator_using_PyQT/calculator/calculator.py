from PyQt5 import QtWidgets
from homework.topic_21_creating_a_calculator_using_PyQT.calculator.ui_calculator import Ui_Calculator

__version__ = 2.0
__author__ = 'Oleh Komenchuk'


class CalculatorWindow(QtWidgets.QMainWindow, Ui_Calculator):
    firstNum = None
    userIsTypingSecondNumber = False

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        # Connect buttons
        self.pushButton_0.clicked.connect(self.digit_pressed)
        self.pushButton_1.clicked.connect(self.digit_pressed)
        self.pushButton_2.clicked.connect(self.digit_pressed)
        self.pushButton_3.clicked.connect(self.digit_pressed)
        self.pushButton_4.clicked.connect(self.digit_pressed)
        self.pushButton_5.clicked.connect(self.digit_pressed)
        self.pushButton_6.clicked.connect(self.digit_pressed)
        self.pushButton_7.clicked.connect(self.digit_pressed)
        self.pushButton_8.clicked.connect(self.digit_pressed)
        self.pushButton_9.clicked.connect(self.digit_pressed)

        self.pushButton_decimal.clicked.connect(self.decimal_pressed)

        self.pushButton_plusMinus.clicked.connect(self.unary_operation_pressed)
        self.pushButton_percent.clicked.connect(self.unary_operation_pressed)

        self.pushButton_add.clicked.connect(self.binary_operation_pressed)
        self.pushButton_subtract.clicked.connect(self.binary_operation_pressed)
        self.pushButton_multiply.clicked.connect(self.binary_operation_pressed)
        self.pushButton_divide.clicked.connect(self.binary_operation_pressed)

        self.pushButton_equals.clicked.connect(self.equals_pressed)
        self.pushButton_clear.clicked.connect(self.clear_pressed)

        self.pushButton_add.setCheckable(True)
        self.pushButton_subtract.setCheckable(True)
        self.pushButton_multiply.setCheckable(True)
        self.pushButton_divide.setCheckable(True)

    def digit_pressed(self):
        button = self.sender()

        if ((self.pushButton_add.isChecked() or self.pushButton_subtract.isChecked() or
             self.pushButton_multiply.isChecked() or self.pushButton_divide.isChecked()) and (
                not self.userIsTypingSecondNumber)):
            newLabel = format(float(button.text()), '.15g')
            self.userIsTypingSecondNumber = True
        else:
            if (('.' in self.label.text()) and (button.text() == '0')):
                newLabel = format(self.label.text() + button.text(), '.15')
            else:
                newLabel = format(float(self.label.text() + button.text()), '.15g')

        self.label.setText(newLabel)

    def decimal_pressed(self):
        self.label.setText(self.label.text() + '.')

    def unary_operation_pressed(self):
        button = self.sender()

        labelNumber = float(self.label.text())

        if button.text() == '+/-':
            labelNumber = labelNumber * -1
        else:  # button text == %
            labelNumber = labelNumber * 0.01

        newLabel = format(labelNumber, '.15g')
        self.label.setText(newLabel)

    def binary_operation_pressed(self):
        button = self.sender()

        self.firstNum = float(self.label.text())

        button.setChecked(True)

    def equals_pressed(self):
        secondNum = float(self.label.text())

        if self.pushButton_add.isChecked():
            labelNumber = self.firstNum + secondNum
            newLabel = format(labelNumber, '.15g')
            self.label.setText(newLabel)
            self.pushButton_add.setChecked(False)
        elif self.pushButton_subtract.isChecked():
            labelNumber = self.firstNum - secondNum
            newLabel = format(labelNumber, '.15g')
            self.label.setText(newLabel)
            self.pushButton_subtract.setChecked(False)
        if self.pushButton_multiply.isChecked():
            labelNumber = self.firstNum * secondNum
            newLabel = format(labelNumber, '.15g')
            self.label.setText(newLabel)
            self.pushButton_multiply.setChecked(False)
        if self.pushButton_divide.isChecked():
            labelNumber = self.firstNum / secondNum
            newLabel = format(labelNumber, '.15g')
            self.label.setText(newLabel)
            self.pushButton_divide.setChecked(False)

        self.userIsTypingSecondNumber = False

    def clear_pressed(self):
        self.pushButton_add.setChecked(False)
        self.pushButton_subtract.setChecked(False)
        self.pushButton_multiply.setChecked(False)
        self.pushButton_divide.setChecked(False)

        self.userIsTypingSecondNumber = False

        self.label.setText('0')
