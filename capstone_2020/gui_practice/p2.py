# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'p2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(464, 382)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ok_button = QtWidgets.QPushButton(self.centralwidget)
        self.ok_button.setGeometry(QtCore.QRect(270, 170, 91, 41))
        self.ok_button.setObjectName("ok_button")
        self.mov_name = QtWidgets.QTextEdit(self.centralwidget)
        self.mov_name.setGeometry(QtCore.QRect(240, 120, 121, 21))
        self.mov_name.setObjectName("mov_name")
        self.ques1 = QtWidgets.QLabel(self.centralwidget)
        self.ques1.setGeometry(QtCore.QRect(100, 120, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.ques1.setFont(font)
        self.ques1.setObjectName("ques1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 464, 21))
        self.menubar.setObjectName("menubar")
        self.menuabout = QtWidgets.QMenu(self.menubar)
        self.menuabout.setObjectName("menuabout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionMovie_Rater_1_0 = QtWidgets.QAction(MainWindow)
        self.actionMovie_Rater_1_0.setObjectName("actionMovie_Rater_1_0")
        self.menuabout.addAction(self.actionMovie_Rater_1_0)
        self.menubar.addAction(self.menuabout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.ok_button.clicked.connect(self.on_click)
        self.actionMovie_Rater_1_0.triggered.connect(lambda: self.show_popup("Movie Rater", "Movie Rater\nVersion 1.0"))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Movie Rater"))
        self.ok_button.setText(_translate("MainWindow", "OK"))
        self.ok_button.setShortcut(_translate("MainWindow", "Enter"))
        self.ques1.setText(_translate("MainWindow", "Enter a Movie Name"))
        self.mov_name.setText(_translate("MainWindow", "Enter Text here"))
        self.menuabout.setTitle(_translate("MainWindow", "About"))
        self.actionMovie_Rater_1_0.setText(_translate("MainWindow", "Movie Rater 1.0"))

    def show_popup(self, title, text):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(text)
        if title == "Error":
            msg.setIcon(QMessageBox.Critical)
            msg.setStandardButtons(QMessageBox.Retry)
        else:
            msg.setIcon(QMessageBox.Information)

        x = msg.exec_()

    def on_click(self):
        movie_name = self.mov_name.toPlainText()
        if movie_name == "Enter Text here":
            self.show_popup("Error", "You have not Entered a movie name")
        else:
            print(movie_name)



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
