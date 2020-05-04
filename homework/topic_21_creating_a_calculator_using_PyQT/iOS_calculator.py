"""-----Creating a simple iOS calculator using PyQt5-----"""
import sys

# Импорт необходимых модулей и классов из PyQt5.QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from functools import partial

__version__ = 1.0
__author__ = 'Oleh Komenchuk'


# Создание графического интерфейса с классом PyCalcUi
class PyCalcUi(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('iOS Calculator')  # Устанавливает заголовок окна в PyCalc
        self.setFixedSize(235, 235)  # Придает окну фиксированый размер
        # Создает QWidget объект, который играет роль центрального виджета
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        # Создание кнопок и дисплея
        self._createDisplay()
        self._createButtons()

    def _createDisplay(self):
        self.display = QLineEdit()
        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)

    def _createButtons(self):
        self.buttons = {}
        buttonsLayout = QGridLayout()
        buttons = {
            'C': (0, 0),
            '+/-': (0, 1),
            '%': (0, 2),
            '/': (0, 3),
            '7': (1, 0),
            '8': (1, 1),
            '9': (1, 2),
            '*': (1, 3),
            '4': (2, 0),
            '5': (2, 1),
            '6': (2, 2),
            '-': (2, 3),
            '1': (3, 0),
            '2': (3, 1),
            '3': (3, 2),
            '+': (3, 3),
            '0': (4, 0, 1, 2),  # (4, 0, 1, 2)
            '.': (4, 2),
            '=': (4, 3)
        }
        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(40, 40)
            buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])
            self.generalLayout.addLayout(buttonsLayout)

    def setDisplayText(self, text):
        self.display.setText(text)
        self.display.setFocus()

    def displayText(self):
        return self.display.text()

    def clearDisplay(self):
        self.setDisplayText('')


class PyCalcCtrl:
    def __init__(self, model, view):
        self._evaluate = model
        self._view = view
        self._connectSignals()

    def _calculateResult(self):
        result = self._evaluate(expression=self._view.displayText())
        self._view.setDisplayText(result)

    def _buildExpression(self, sub_exp):
        if self._view.displayText() == ERROR_MSG:
            self._view.clearDisplay()

        expression = self._view.displayText() + sub_exp
        self._view.setDisplayText(expression)

    def _changeSignClicked(self):
        text = self._view.displayText()
        value = float(text)

        if value > 0.0:
            text = '-' + text
        elif value < 0.0:
            text = text[1:]

        self.display.setText(text)

    def _connectSignals(self):
        for btnText, btn in self._view.buttons.items():
            if btnText not in {'=', 'C', '+/-'}:
                btn.clicked.connect(partial(self._buildExpression, btnText))

        self._view.buttons['='].clicked.connect(self._calculateResult)
        self._view.display.returnPressed.connect(self._calculateResult)
        self._view.buttons['C'].clicked.connect(self._view.clearDisplay)
        self._view.buttons['+/-'].clicked.connect(self._changeSignClicked)


ERROR_MSG = 'ERROR'


def eveluateExpression(expression):
    try:
        result = str(eval(expression, {}, {}))
    except Exception:
        result = ERROR_MSG

    return result


# Определяет основную функцию калькулятора
def main():
    pycalc = QApplication(sys.argv)
    view = PyCalcUi()
    view.show()
    model = eveluateExpression
    PyCalcCtrl(model=model, view=view)
    sys.exit(pycalc.exec_())


if __name__ == "__main__":
    main()
