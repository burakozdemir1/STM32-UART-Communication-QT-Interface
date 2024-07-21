# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'serial_terminal.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(31, 31, 31);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(31, 31, 31);\n"
"color: rgb(108, 108, 108);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.Terminal = QtWidgets.QTextBrowser(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setBold(True)
        font.setWeight(75)
        self.Terminal.setFont(font)
        self.Terminal.setStyleSheet("background-color: rgb(31, 31, 31);\n"
"color: rgb(108, 108, 108);")
        self.Terminal.setObjectName("Terminal")
        self.verticalLayout_2.addWidget(self.Terminal)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.input = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.input.setFont(font)
        self.input.setStyleSheet("background-color: rgb(31, 31, 31);\n"
"color: rgb(108, 108, 108);\n"
"alternate-background-color: rgb(0, 0, 0);\n"
"border-color: rgb(17, 17, 17);")
        self.input.setObjectName("input")
        self.horizontalLayout_4.addWidget(self.input)
        self.sendBtn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.sendBtn.setFont(font)
        self.sendBtn.setStyleSheet("background-color: rgb(31, 31, 31);\n"
"color: rgb(108, 108, 108);")
        self.sendBtn.setObjectName("sendBtn")
        self.horizontalLayout_4.addWidget(self.sendBtn)
        self.clearBtn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.clearBtn.setFont(font)
        self.clearBtn.setStyleSheet("background-color: rgb(31, 31, 31);\n"
"color: rgb(108, 108, 108);")
        self.clearBtn.setObjectName("clearBtn")
        self.horizontalLayout_4.addWidget(self.clearBtn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setStyleSheet("border-image: url(:/yeni/SdBzdDgFRJC9X8ppW678Ww.jpg);")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.verticalLayout_3.addWidget(self.textBrowser_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(31, 31, 31);\n"
"color: rgb(108, 108, 108);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.portList = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.portList.setFont(font)
        self.portList.setStyleSheet("background-color: rgb(31, 31, 31);\n"
"color: rgb(108, 108, 108);")
        self.portList.setObjectName("portList")
        self.horizontalLayout.addWidget(self.portList)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(31, 31, 31);\n"
"color: rgb(108, 108, 108);")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.BaudList = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.BaudList.setFont(font)
        self.BaudList.setStyleSheet("background-color: rgb(31, 31, 31);\n"
"color: rgb(108, 108, 108);")
        self.BaudList.setObjectName("BaudList")
        self.horizontalLayout_2.addWidget(self.BaudList)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.connectBtn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.connectBtn.setFont(font)
        self.connectBtn.setStyleSheet("#connectBtn\n"
"{\n"
"color: rgb(108, 108, 108);\n"
"}\n"
"#connectBtn:checked{\n"
"background-color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.connectBtn.setCheckable(True)
        self.connectBtn.setObjectName("connectBtn")
        self.horizontalLayout_3.addWidget(self.connectBtn)
        self.updateBtn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.updateBtn.setFont(font)
        self.updateBtn.setStyleSheet("background-color: rgb(31, 31, 31);\n"
"color: rgb(108, 108, 108);")
        self.updateBtn.setObjectName("updateBtn")
        self.horizontalLayout_3.addWidget(self.updateBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7.addLayout(self.verticalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_6.setText(_translate("MainWindow", "TERMINAL SERIAL"))
        self.sendBtn.setText(_translate("MainWindow", "SEND"))
        self.clearBtn.setText(_translate("MainWindow", "CLEAR"))
        self.label_2.setText(_translate("MainWindow", "Port:"))
        self.label_3.setText(_translate("MainWindow", "Baud Rate:"))
        self.connectBtn.setText(_translate("MainWindow", "CONNECT"))
        self.updateBtn.setText(_translate("MainWindow", "UPDATE"))
import yeni_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
