import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

#ADD IMPORT STATEMENT FOR YOUR GENERATED UI.PY FILE HERE
import SavePeople_Lib

#CHANGE THE SECOND PARAMETER HERE TO MATCH YOUR GENERATED UI.PY FILE
class MyForm(QMainWindow, SavePeople_Lib.Ui_MainWindow):

    peopleList = [] #Global 2D list
    unsavedChanges = False

        # DO NOT MODIFY THIS CODE
    def __init__(self, parent=None):
        super(MyForm, self).__init__(parent)
        self.setupUi(self)
        # END DO NOT MODIFY

        # ADD SLOTS HERE
        self.listWidgetPeople.currentRowChanged.connect(self.List_RowChanged)
        self.pushButtonUpdate.clicked.connect(self.UpdateButton_Clicked)
        self.actionSave_to_File.triggered.connect(self.SaveAction_Triggered)
        self.actionExit.triggered.connect(self.ExitAction_Triggered)

        self.LoadDataFromFile()
        self.LoadListWidget()

    # ADD SLOT FUNCTIONS HERE
    def List_RowChanged(self, newIndex):
        self.lineEditName.setText(self.peopleList[newIndex][0])
        self.lineEditAge.setText(self.peopleList[newIndex][1])

    def UpdateButton_Clicked(self):
        self.unsavedChanges = True
        self.SaveToMemory()

        #Display a popup message
        QMessageBox.information(self, "Geoff's Title Bar", \
                                "Your changes have been saved to memory, hurray!", \
                                QMessageBox.Ok)

    def SaveAction_Triggered(self):
        if self.unsavedChanges == True:

            reply = QMessageBox.question(self, "Save?", \
                                 "Are you REALLY sure you want save?", \
                                 QMessageBox.Yes, QMessageBox.No)

            if reply == QMessageBox.Yes:
                self.SaveToFile()

    def ExitAction_Triggered(self):
        if self.unsavedChanges == True:

            reply = QMessageBox.question(self, "Save?", \
                                 "Are you REALLY sure you want save?", \
                                 QMessageBox.Yes, QMessageBox.No)

            if reply == QMessageBox.Yes:
                self.SaveToFile()
        QApplication.closeAllWindows()

    #ADD HELPER FUNCTIONS HERE
    def SaveToFile(self):
        with open("People.txt", "w") as myFile:
            for row in self.peopleList:
                myFile.write(",".join(row) + " \n")

    def SaveToMemory(self):
        selectedIndex = self.listWidgetPeople.currentRow()
        name = self.lineEditName.text()
        age = self.lineEditAge.text()

        self.peopleList[selectedIndex][0] = name
        self.peopleList[selectedIndex][1] = age

        self.LoadListWidget()

        self.listWidgetPeople.setCurrentRow(selectedIndex)

    def LoadDataFromFile(self):
        import csv

        with open("People.txt", "r") as myFile:
            theData = csv.reader(myFile)

            self.peopleList = []
            for row in theData:
                self.peopleList.append(row)

    def LoadListWidget(self):
        self.listWidgetPeople.clear()
        for person in self.peopleList:
            self.listWidgetPeople.addItem(person[0])

# DO NOT MODIFY THIS CODE
if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_form = MyForm()
    the_form.show()
    sys.exit(app.exec_())
# END DO NOT MODIFY
