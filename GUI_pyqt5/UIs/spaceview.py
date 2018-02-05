# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spaceview.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.myLabel = QtWidgets.QLabel(self.centralwidget)
        self.myLabel.setGeometry(QtCore.QRect(110, 100, 421, 221))
        self.myLabel.setText("")
        self.myLabel.setPixmap(QtGui.QPixmap("../imgs/space1.jpg"))
        self.myLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.myLabel.setObjectName("myLabel")
        self.next_btn = QtWidgets.QPushButton(self.centralwidget)
        self.next_btn.setGeometry(QtCore.QRect(540, 147, 93, 131))
        self.next_btn.setObjectName("next_btn")
        self.prev_btn = QtWidgets.QPushButton(self.centralwidget)
        self.prev_btn.setGeometry(QtCore.QRect(10, 140, 93, 131))
        self.prev_btn.setObjectName("prev_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 26))
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
        self.next_btn.setText(_translate("MainWindow", "NEXT"))
        self.prev_btn.setText(_translate("MainWindow", "PREV"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

