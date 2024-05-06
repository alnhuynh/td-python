import sys
# from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

class MyBombWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("New Window")
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)
        self.create_widgets()

    def create_widgets(self):
        self.label1 = QLabel("Different Widget examples:", self)
        self.label2 = QLabel("An entry example:", self)
        self.label3 = QLabel("A checkbox example:", self)
        self.label4 = QLabel("A radiobutton example:", self)
        self.label5 = QLabel("A listbox with scrollbar example:", self)
        self.label6 = QLabel("A slider example:", self)
        self.label7 = QLabel("A multi-line text example:", self)
        self.label8 = QLabel("A button example:", self)

        self.entry_widget = QLineEdit(self)

        self.checkbox_widget = QCheckBox("Smart", self)

        self.armed_radio = QRadioButton("Armed", self)
        self.disarmed_radio = QRadioButton("Disarmed", self)
        self.radio_button_group = QButtonGroup(self)
        self.radio_button_group.addButton(self.armed_radio)
        self.radio_button_group.addButton(self.disarmed_radio)

        self.list_widget = QListWidget(self)
        self.list_widget.addItems(["Small", "Medium", "Large", "Mondo", "Gargantuan", "Wow"])
        self.scrollbar = QScrollBar(self)
        self.scrollbar.setOrientation(1)

        self.slider_widget = QSlider(1, self)
        self.slider_widget.setOrientation(1)
        self.slider_widget.setTickInterval(25)
        self.slider_widget.setTickPosition(2)

        self.text_widget = QTextEdit(self)

        self.button_widget = QPushButton("Boom", self)

        self.layout.addWidget(self.label1)
        self.layout.addWidget(self.label2)
        self.layout.addWidget(self.entry_widget)
        self.layout.addWidget(self.label3)
        self.layout.addWidget(self.checkbox_widget)
        self.layout.addWidget(self.label4)
        self.layout.addWidget(self.armed_radio)
        self.layout.addWidget(self.disarmed_radio)
        self.layout.addWidget(self.label5)
        self.layout.addWidget(self.list_widget)
        self.layout.addWidget(self.scrollbar)
        self.layout.addWidget(self.label6)
        self.layout.addWidget(self.slider_widget)
        self.layout.addWidget(self.label7)
        self.layout.addWidget(self.text_widget)
        self.layout.addWidget(self.label8)
        self.layout.addWidget(self.button_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyBombWindow()
    window.setGeometry(100, 100, 400, 400)
    window.show()
    sys.exit(app.exec_())
