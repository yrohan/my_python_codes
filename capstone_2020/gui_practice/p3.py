# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'p3.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication
import sys
import time


class Ui_sec_Window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(464, 382)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame2 = QtWidgets.QFrame(self.centralwidget)
        self.frame2.setGeometry(QtCore.QRect(40, 10, 325, 231))
        self.frame2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame2.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame2)
        self.label.setGeometry(QtCore.QRect(100, 70, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(self.frame2)
        self.progressBar.setGeometry(QtCore.QRect(40, 140, 290, 25))
        self.progressBar.setRange(0, 100)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
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
        self.actionMovie_Rater_1_0.triggered.connect(lambda: self.show_popup("About", "Movie Rater\nVersion 1.0"))
        self.inc_prog_bar()
        return self.progressBar.value()

    def inc_prog_bar(self):
        for i in range(0, 101):
            if i == 0:
                self.label.adjustSize()
            elif i % 2 == 0:
                self.label.setText("Loading Result /")
            else:
                self.label.setText("Loading Result \\")
            self.label.adjustSize()
            self.progressBar.setValue(i)
            QApplication.processEvents()
            time.sleep(0.5)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Movie Rater"))
        self.label.setText(_translate("MainWindow", "Loading Results"))
        self.label.adjustSize()
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


class Ui_third_Window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(464, 382)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame3 = QtWidgets.QFrame(self.centralwidget)
        self.frame3.setGeometry(QtCore.QRect(20, 20, 431, 301))
        self.frame3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame3.setObjectName("frame3")
        self.label_2 = QtWidgets.QLabel(self.frame3)
        self.label_2.setGeometry(QtCore.QRect(190, 50, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame3)
        self.label_3.setGeometry(QtCore.QRect(90, 80, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame3)
        self.label_4.setGeometry(QtCore.QRect(90, 110, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame3)
        self.label_5.setGeometry(QtCore.QRect(90, 140, 47, 13))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame3)
        self.label_6.setGeometry(QtCore.QRect(90, 170, 47, 13))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame3)
        self.label_7.setGeometry(QtCore.QRect(90, 200, 47, 13))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame3)
        self.label_8.setGeometry(QtCore.QRect(90, 240, 47, 13))
        self.label_8.setObjectName("label_8")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_3.setFont(font)
        self.label_4.setFont(font)
        self.label_5.setFont(font)
        self.label_6.setFont(font)
        self.label_7.setFont(font)
        self.label_8.setFont(font)
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

        self.actionMovie_Rater_1_0.triggered.connect(lambda: self.show_popup("About", "Movie Rater\nVersion 1.0"))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Movie Rater"))
        self.label_2.setText(_translate("MainWindow", "Movie Ratings"))
        self.label_3.setText(_translate("MainWindow", "Acting"))
        self.label_4.setText(_translate("MainWindow", "Plot"))
        self.label_5.setText(_translate("MainWindow", "Sound"))
        self.label_6.setText(_translate("MainWindow", ""))
        self.label_7.setText(_translate("MainWindow", ""))
        self.label_8.setText(_translate("MainWindow", "Overall Rating"))
        self.label_2.adjustSize()
        self.label_3.adjustSize()
        self.label_4.adjustSize()
        self.label_5.adjustSize()
        self.label_6.adjustSize()
        self.label_7.adjustSize()
        self.label_8.adjustSize()
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


class Ui_MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)
        self.setObjectName("MainWindow")
        self.resize(464, 382)
        self.sec_window = Ui_sec_Window()
        self.third_window = Ui_third_Window()
        self.setupUi()

    def setupUi(self):
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.frame1 = QtWidgets.QFrame(self.centralwidget)
        self.frame1.setGeometry(QtCore.QRect(40, 40, 381, 261))
        self.frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame1.setObjectName("frame1")
        self.mov_name = QtWidgets.QTextEdit(self.frame1)
        self.mov_name.setGeometry(QtCore.QRect(190, 80, 141, 21))
        self.mov_name.setObjectName("textEdit")
        self.ok_button = QtWidgets.QPushButton(self.frame1)
        self.ok_button.setGeometry(QtCore.QRect(270, 170, 91, 41))
        self.ok_button.setObjectName("ok_button")
        self.ques1 = QtWidgets.QLabel(self.frame1)
        self.ques1.setGeometry(QtCore.QRect(55, 80, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.ques1.setFont(font)
        self.ques1.setObjectName("ques1")

        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 464, 21))
        self.menubar.setObjectName("menubar")
        self.menuabout = QtWidgets.QMenu(self.menubar)
        self.menuabout.setObjectName("menuabout")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.actionMovie_Rater_1_0 = QtWidgets.QAction(self)
        self.actionMovie_Rater_1_0.setObjectName("actionMovie_Rater_1_0")
        self.menuabout.addAction(self.actionMovie_Rater_1_0)
        self.menubar.addAction(self.menuabout.menuAction())

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.actionMovie_Rater_1_0.triggered.connect(lambda: self.show_popup("About", "Movie Rater\nVersion 1.0"))
        self.ok_button.clicked.connect(self.on_click)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Movie Rater"))
        self.ok_button.setText(_translate("MainWindow", "OK"))
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

    def switch_to_third(self):
        self.third_window.setupUi(self)
        self.show()

    def switch_to_sec(self):
        progress = self.sec_window.setupUi(self)
        self.show()
        if progress == 100:
            self.switch_to_third()

    def on_click(self):
        movie_name = self.mov_name.toPlainText()
        if movie_name == "Enter Text here":
            self.show_popup("Error", "You have not Entered a movie name")
        else:
            print(movie_name)
            self.switch_to_sec()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()

    ui.show()
    sys.exit(app.exec_())
