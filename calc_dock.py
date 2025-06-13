from qgis.PyQt.QtWidgets import (
    QWidget,
    QLineEdit,
    QAbstractItemView,
    QDockWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
)
from qgis.PyQt.QtCore import Qt
from qgis.utils import iface


class CalcDock(QDockWidget):
    def __init__(self, iface):
        super().__init__()
        self.setObjectName('SimpleCalc')
        self.setWindowTitle('Simple Calc')
        self.iface = iface
        
        self.widget = QWidget()
        self.ovr_layout = QVBoxLayout()
        
        self.input_line = QLineEdit()
        self.ovr_layout.addWidget(self.input_line)
        self.results_line = QLineEdit()
        self.results_line.setReadOnly(True)
        self.ovr_layout.addWidget(self.results_line)
        
        self.button_layout_1 = QHBoxLayout()
        
        self.right_paren_button = QPushButton("(")
        self.right_paren_button.clicked.connect(lambda: self.sendText(self.right_paren_button))
        self.button_layout_1.addWidget(self.right_paren_button)

        self.left_paren_button = QPushButton(")")
        self.left_paren_button.clicked.connect(lambda: self.sendText(self.left_paren_button))
        self.button_layout_1.addWidget(self.left_paren_button)

        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect(self.clearText)
        self.button_layout_1.addWidget(self.clear_button)

        self.bsp_button = QPushButton("Backspace")
        self.bsp_button.clicked.connect(self.bspAction)
        self.button_layout_1.addWidget(self.bsp_button)

        self.ovr_layout.addLayout(self.button_layout_1)

        self.button_layout_2 = QHBoxLayout()

        self.onex_button = QPushButton("1/x")
        self.onex_button.clicked.connect(self.oneX)
        self.button_layout_2.addWidget(self.onex_button)

        self.power_button = QPushButton("^")
        self.power_button.clicked.connect(lambda: self.sendText(self.power_button))
        self.button_layout_2.addWidget(self.power_button)

        self.sqrt_button = QPushButton("sqrt")
        self.sqrt_button.clicked.connect(self.sqrt)
        self.button_layout_2.addWidget(self.sqrt_button)

        self.div_button = QPushButton("/")
        self.div_button.clicked.connect(lambda: self.sendText(self.div_button))
        self.button_layout_2.addWidget(self.div_button)

        self.ovr_layout.addLayout(self.button_layout_2)

        self.button_layout_3 = QHBoxLayout()

        self.seven_button = QPushButton("7")
        self.seven_button.clicked.connect(lambda: self.sendText(self.seven_button))
        self.button_layout_3.addWidget(self.seven_button)

        self.eight_button = QPushButton("8")
        self.eight_button.clicked.connect(lambda: self.sendText(self.eight_button))
        self.button_layout_3.addWidget(self.eight_button)

        self.nine_button = QPushButton("9")
        self.nine_button.clicked.connect(lambda: self.sendText(self.nine_button))
        self.button_layout_3.addWidget(self.nine_button)

        self.mult_button = QPushButton("*")
        self.mult_button.clicked.connect(lambda: self.sendText(self.mult_button))
        self.button_layout_3.addWidget(self.mult_button)

        self.ovr_layout.addLayout(self.button_layout_3)

        self.button_layout_4 = QHBoxLayout()

        self.four_button = QPushButton("4")
        self.four_button.clicked.connect(lambda: self.sendText(self.four_button))
        self.button_layout_4.addWidget(self.four_button)

        self.five_button = QPushButton("5")
        self.five_button.clicked.connect(lambda: self.sendText(self.five_button))
        self.button_layout_4.addWidget(self.five_button)

        self.six_button = QPushButton("6")
        self.six_button.clicked.connect(lambda: self.sendText(self.six_button))
        self.button_layout_4.addWidget(self.six_button)

        self.minus_button = QPushButton("-")
        self.minus_button.clicked.connect(lambda: self.sendText(self.minus_button))
        self.button_layout_4.addWidget(self.minus_button)

        self.ovr_layout.addLayout(self.button_layout_4)

        self.button_layout_5 = QHBoxLayout()

        self.one_button = QPushButton("1")
        self.one_button.clicked.connect(lambda: self.sendText(self.one_button))
        self.button_layout_5.addWidget(self.one_button)

        self.two_button = QPushButton("2")
        self.two_button.clicked.connect(lambda: self.sendText(self.two_button))
        self.button_layout_5.addWidget(self.two_button)

        self.three_button = QPushButton("3")
        self.three_button.clicked.connect(lambda: self.sendText(self.three_button))
        self.button_layout_5.addWidget(self.three_button)

        self.plus_button = QPushButton("+")
        self.plus_button.clicked.connect(lambda: self.sendText(self.plus_button))
        self.button_layout_5.addWidget(self.plus_button)

        self.ovr_layout.addLayout(self.button_layout_5)

        self.button_layout_6 = QHBoxLayout()

        self.plmi_button = QPushButton("+/-")
        self.plmi_button.clicked.connect(self.plmi)
        self.button_layout_6.addWidget(self.plmi_button)

        self.zero_button = QPushButton("0")
        self.zero_button.clicked.connect(lambda: self.sendText(self.zero_button))
        self.button_layout_6.addWidget(self.zero_button)

        self.dec_button = QPushButton(".")
        self.dec_button.clicked.connect(lambda: self.sendText(self.dec_button))
        self.button_layout_6.addWidget(self.dec_button)

        self.equals_button = QPushButton("=")
        self.equals_button.clicked.connect(self.evaluate)
        self.button_layout_6.addWidget(self.equals_button)

        self.ovr_layout.addLayout(self.button_layout_6)

    def evaluate(self):
        pass

    def plmi(self):
        pass

    def sqrt(self):
        pass

    def oneX(self):
        pass

    def sendText(self, button):
        char = button.text()
        old_text = self.input_line.text()
        new_text = old_text + char
        self.input_line.setText(new_text)

    def clearText(self):
        self.input_line.setText("")

    def bspAction(self):
        old_text = self.input_line.text()
        new_text = old_text[0:-1]
        self.input_line.setText(new_text)
