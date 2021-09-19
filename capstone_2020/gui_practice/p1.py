from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle("MY Program")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("my first label!")
        self.label.move(150, 140)
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click Me")
        self.b1.move(10, 250)
        self.b1.clicked.connect(self.on_click)

    def on_click(self):
        self.label.setText("You have pressed the button.")
        self.update()

    def update(self):
        self.label.move(130,140)
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
