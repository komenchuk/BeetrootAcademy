import sys
from PyQt5.QtWidgets import QApplication
from homework.topic_21_creating_a_calculator_using_PyQT.calculator.calculator import CalculatorWindow

app = QApplication(sys.argv)

calculator = CalculatorWindow()

sys.exit(app.exec_())
