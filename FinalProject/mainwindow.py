# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cow_mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(754, 689)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_instruction = QtWidgets.QLabel(self.centralwidget)
        self.label_instruction.setGeometry(QtCore.QRect(20, 10, 231, 20))
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_instruction.setFont(font)
        self.label_instruction.setObjectName("label_instruction")
        self.widget_countryinfo = QtWidgets.QWidget(self.centralwidget)
        self.widget_countryinfo.setEnabled(True)
        self.widget_countryinfo.setGeometry(QtCore.QRect(300, 30, 451, 601))
        self.widget_countryinfo.setStatusTip("")
        self.widget_countryinfo.setObjectName("widget_countryinfo")
        self.label_countryname = QtWidgets.QLabel(self.widget_countryinfo)
        self.label_countryname.setGeometry(QtCore.QRect(10, 10, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_countryname.setFont(font)
        self.label_countryname.setObjectName("label_countryname")
        self.label_population = QtWidgets.QLabel(self.widget_countryinfo)
        self.label_population.setGeometry(QtCore.QRect(20, 280, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_population.setFont(font)
        self.label_population.setObjectName("label_population")
        self.label_area = QtWidgets.QLabel(self.widget_countryinfo)
        self.label_area.setGeometry(QtCore.QRect(20, 320, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_area.setFont(font)
        self.label_area.setObjectName("label_area")
        self.comboBox_unit = QtWidgets.QComboBox(self.widget_countryinfo)
        self.comboBox_unit.setGeometry(QtCore.QRect(100, 330, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox_unit.setFont(font)
        self.comboBox_unit.setObjectName("comboBox_unit")
        self.comboBox_unit.addItem("")
        self.comboBox_unit.addItem("")
        self.label_numberofarea = QtWidgets.QLabel(self.widget_countryinfo)
        self.label_numberofarea.setGeometry(QtCore.QRect(220, 330, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_numberofarea.setFont(font)
        self.label_numberofarea.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_numberofarea.setObjectName("label_numberofarea")
        self.groupBox_density = QtWidgets.QGroupBox(self.widget_countryinfo)
        self.groupBox_density.setGeometry(QtCore.QRect(30, 370, 391, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_density.setFont(font)
        self.groupBox_density.setObjectName("groupBox_density")
        self.radioButton_sqmiles = QtWidgets.QRadioButton(self.groupBox_density)
        self.radioButton_sqmiles.setGeometry(QtCore.QRect(20, 30, 181, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_sqmiles.setFont(font)
        self.radioButton_sqmiles.setChecked(True)
        self.radioButton_sqmiles.setObjectName("radioButton_sqmiles")
        self.radioButton_sqkm = QtWidgets.QRadioButton(self.groupBox_density)
        self.radioButton_sqkm.setGeometry(QtCore.QRect(20, 50, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_sqkm.setFont(font)
        self.radioButton_sqkm.setObjectName("radioButton_sqkm")
        self.label_numberofdensity = QtWidgets.QLabel(self.groupBox_density)
        self.label_numberofdensity.setGeometry(QtCore.QRect(206, 30, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_numberofdensity.setFont(font)
        self.label_numberofdensity.setText("")
        self.label_numberofdensity.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_numberofdensity.setObjectName("label_numberofdensity")
        self.label_percentage = QtWidgets.QLabel(self.widget_countryinfo)
        self.label_percentage.setGeometry(QtCore.QRect(20, 460, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_percentage.setFont(font)
        self.label_percentage.setObjectName("label_percentage")
        self.label_numberofper = QtWidgets.QLabel(self.widget_countryinfo)
        self.label_numberofper.setGeometry(QtCore.QRect(260, 470, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_numberofper.setFont(font)
        self.label_numberofper.setText("")
        self.label_numberofper.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_numberofper.setObjectName("label_numberofper")
        self.label_countryflag = QtWidgets.QLabel(self.widget_countryinfo)
        self.label_countryflag.setGeometry(QtCore.QRect(30, 60, 391, 181))
        self.label_countryflag.setText("")
        self.label_countryflag.setObjectName("label_countryflag")
        self.pushButton_save = QtWidgets.QPushButton(self.widget_countryinfo)
        self.pushButton_save.setGeometry(QtCore.QRect(22, 527, 401, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_save.setFont(font)
        self.pushButton_save.setObjectName("pushButton_save")
        self.textEdit_population = QtWidgets.QLineEdit(self.widget_countryinfo)
        self.textEdit_population.setGeometry(QtCore.QRect(160, 280, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_population.setFont(font)
        self.textEdit_population.setObjectName("textEdit_population")
        self.listWidget_countries = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_countries.setGeometry(QtCore.QRect(10, 30, 281, 601))
        self.listWidget_countries.setObjectName("listWidget_countries")
        self.widget_countryinfo.raise_()
        self.label_instruction.raise_()
        self.listWidget_countries.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 754, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad_Countries = QtWidgets.QAction(MainWindow)
        self.actionLoad_Countries.setObjectName("actionLoad_Countries")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionSave_Countries = QtWidgets.QAction(MainWindow)
        self.actionSave_Countries.setObjectName("actionSave_Countries")
        self.menuFile.addAction(self.actionLoad_Countries)
        self.menuFile.addAction(self.actionSave_Countries)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.comboBox_unit.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_instruction.setText(_translate("MainWindow", "Chose a country from the list"))
        self.label_countryname.setText(_translate("MainWindow", "Country Name"))
        self.label_population.setText(_translate("MainWindow", "Population:"))
        self.label_area.setText(_translate("MainWindow", "Area in"))
        self.comboBox_unit.setCurrentText(_translate("MainWindow", "Sq. Miles"))
        self.comboBox_unit.setItemText(0, _translate("MainWindow", "Sq. Miles"))
        self.comboBox_unit.setItemText(1, _translate("MainWindow", "Sq. Km"))
        self.label_numberofarea.setText(_translate("MainWindow", ":"))
        self.groupBox_density.setTitle(_translate("MainWindow", "Population Density"))
        self.radioButton_sqmiles.setText(_translate("MainWindow", "Per Square Miles"))
        self.radioButton_sqkm.setText(_translate("MainWindow", "Per Square KM"))
        self.label_percentage.setText(_translate("MainWindow", "Percentage of\n"
"World Population"))
        self.pushButton_save.setText(_translate("MainWindow", "Update"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionLoad_Countries.setText(_translate("MainWindow", "Load Countries..."))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionSave_Countries.setText(_translate("MainWindow", "Save Countries.."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
