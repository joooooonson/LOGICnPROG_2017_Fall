import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QPixmap

#ADD IMPORT STATEMENT FOR YOUR GENERATED UI.PY FILE HERE
# add main window UI
import mainwindow
# add csv
import csv
#CHANGE THE SECOND PARAMETER HERE TO MATCH YOUR GENERATED UI.PY FILE
class MyForm(QMainWindow, mainwindow.Ui_MainWindow):
    # Auth: Joon Son
    # Date: 2017-12-02
    # Description: main window of Countries of the world APP
    #
    # Pseudocode
    # 1. open file containing country name, number of population, number of are with read only access mode
    # 2. load the countries data into 2d list (=countries)
    # 3. display the information on the APP window
    # 4. allow user to update the 2d list
    # 5. allow user to save the changes by writing the changes on the file
    #
    countries = []
    FILE_PATH = "resource/countries.txt"
    IMG_PATH = "resource/flags/"
    IMG_EXT = ".png"
    MILE_UNIT = 0
    KM_UNIT = 1
    is_changed = False
    # DO NOT MODIFY THIS CODE
    def __init__(self, parent=None):
        super(MyForm, self).__init__(parent)
        self.setupUi(self)
        # END DO NOT MODIFY
        # SET RIGHT PANEL INVISIBLE
        self.widget_countryinfo.hide()

        # ADD SLOTS HERE
        # WHEN CLICK ON [LOAD COUNTRIES]
        self.actionLoad_Countries.triggered.connect(self.push_load_countries)

        # WHEN CHOOSE A ITEM IN THE LIST
            # self.listWidget_countries.currentRowChanged.connect(self.country_selected_from_list)
        self.listWidget_countries.itemSelectionChanged.connect(self.country_selected_from_list)

        # COMBO BOX
        self.comboBox_unit.currentIndexChanged.connect(self.area_in_selected_unit)

        # RADIO BUTTON
        self.radioButton_sqmiles.clicked.connect(self.radio_mile_clicked)
        self.radioButton_sqkm.clicked.connect(self.radio_km_clicked)

        # UPDATE PUSH BUTTON
        self.pushButton_save.clicked.connect(self.update_button_clicked)

        # WHEN CLICK ON [SAVE COUNTRIES]
        self.actionSave_Countries.triggered.connect(self.save_countries)

        # EXIT
        self.actionExit.triggered.connect(self.exit_application)

    # ADD SLOT FUNCTIONS HERE ---------------------------------------------------------------------------------

    def push_load_countries(self):
        # load countries from file to list(countries)
        self.get_coutries_list(self.FILE_PATH)
        # load the name of the countries on list
        if len(self.countries) > 0:
            # when the list exists
            self.populate_countries_list()
            self.widget_countryinfo.hide()
                # self.listWidget_countries.setCurrentRow(0)  # choose first country

            # there is nothing changed
            self.is_changed = False

    def country_selected_from_list(self):
        # get the current selected index
        selectedIndex = self.listWidget_countries.currentRow()
        # display selected country data
        self.display_country_data(selectedIndex)
        # show right frame
        self.widget_countryinfo.show()


    def exit_application(self):
        QApplication.closeAllWindows()

    def area_in_selected_unit(self, selectedIndex):
        self.set_area_in_selected_unit(selectedIndex)

    def radio_mile_clicked(self, enabled):
        if enabled:
            self.set_density_in_selected_unit(self.MILE_UNIT)

    def radio_km_clicked(self, enabled):
        if enabled:
            self.set_density_in_selected_unit(self.KM_UNIT)

    def update_button_clicked(self):
        # update list
        self.update_population()
        # success message
        QMessageBox.information(self, 'Updated', 'Success to update', QMessageBox.Ok)

    def save_countries(self):
        if len(self.countries) >0 and self.is_changed:
            self.save_changes_to_file(self.FILE_PATH)
            self.is_changed = False
            QMessageBox.information(self, 'Save', 'changes saved', QMessageBox.Ok)
        else:
            QMessageBox.information(self, 'Save', 'There is nothing to save', QMessageBox.Ok)

    #ADD HELPER FUNCTIONS HERE ----------------------------------------------------------------------------------

    def get_coutries_list(self, file):
        # initiate countries list
        self.countries.clear()
        # set Access mode as read only
        READ_ACCESS = "r"
        try:
            with open(file,READ_ACCESS,encoding='utf-8-sig') as countriesFile:
                countriesData = csv.reader(countriesFile)
                for country in countriesData:
                    # check validation for data of each country
                    result = self.check_validity(country)
                    if result:
                        self.countries.append(country)
                    else:
                        raise Exception('Invalid File!!!!')
        except FileNotFoundError:
            QMessageBox.information(self, 'Error', 'File was not found', QMessageBox.Ok)
        except Exception:
            QMessageBox.information(self, 'Error', 'This file has invalid country data', QMessageBox.Ok)
            # initialize the list to empty
            self.countries.clear()

    def populate_countries_list(self):
        # initiate test browser
        self.listWidget_countries.clear()
        for country in self.countries:
            # add country's name on text list
            self.listWidget_countries.addItem(country[0])

    def check_validity(self, country):
        result = False
        if len(country)==3:
            try:
                test = float(country[1])
                test = float(country[2])
            except ValueError:
                result = False
            else:
                result = True
        return result


    def display_country_data(self, selected_index):
        # components list
        # [label_countryname]
        # [label_countryflag]
        # [textEdit_population]
        # [label_numberofarea] (default: miles)
        # [label_numberofdensity] (default: miles)
        # [label_numberofper]

        # init setting for combo box and radio button
        self.comboBox_unit.setCurrentIndex(0)
        self.radioButton_sqmiles.setChecked(True)

        # get country name, population, and area
        country_name = self.countries[selected_index][0]
        country_population = self.countries[selected_index][1]
        country_area = self.countries[selected_index][2]+".00"

        # get flag img object
        country_flag_img_path = self.IMG_PATH + country_name.replace(' ','_') + self.IMG_EXT
        country_flag_img = QPixmap(country_flag_img_path )
        country_flag_img = country_flag_img.scaled(390,180)

        # get population density (miles)
        country_population_density = float(country_population) / float(country_area)

        # get world population percentage
        world_population = self.get_total_world_population()
        try:
            country_population_percentage = (int(country_population) / world_population) * 100
        except ZeroDivisionError:
            country_population_percentage = -1
            QMessageBox.information(self, 'Error', 'Wrong World Population!!', QMessageBox.Ok)

        # set the values to the labels on the form
        self.label_countryname.setText(country_name)
        self.textEdit_population.setText(self.thousand_separator(country_population))
        self.label_numberofarea.setText(self.thousand_separator(country_area))
        self.label_countryflag.setPixmap(country_flag_img)
        # self.label_numberofdensity.setText(self.thousand_separator("{:.2f}".format(country_population_density)))
        self.label_numberofdensity.setText("{:,.2f}".format(country_population_density))
        self.label_numberofper.setText("{:.3f}%".format(country_population_percentage))

    def get_total_world_population(self):
        world_population = 0
        for country in self.countries:
            world_population += int(country[1])
        return world_population

    def get_area_in_km(self, areaInMiles):
        area_in_km = float(areaInMiles) * 2.58999
        return area_in_km

    def set_area_in_selected_unit(self, selectedIndex):
        # index 0 : Miles
        # index 1 : Km

        # selected country's index
        currentIndex = self.listWidget_countries.currentRow()

        if selectedIndex == 0:  # miles
            self.label_numberofarea.setText(self.thousand_separator(self.countries[currentIndex][2]+".00"))
        else:  # km
            area_in_km = self.get_area_in_km(self.countries[currentIndex][2])
            self.label_numberofarea.setText("{:,.2f}".format(area_in_km))

    def set_density_in_selected_unit(self, selectedUnit):
        # get current country's population and area
        currentIndex = self.listWidget_countries.currentRow()
        country_population = self.countries[currentIndex][1]
        country_area = ""
        if selectedUnit == self.MILE_UNIT:
            country_area = self.countries[currentIndex][2]
        else:
            country_area = self.get_area_in_km(self.countries[currentIndex][2])
        country_population_density = float(country_population) / float(country_area)
        # show on screen
        self.label_numberofdensity.setText("{:,.2f}".format(country_population_density))

    def \
            update_population(self):
        # get new number of population from line edit
        new_population = self.textEdit_population.text().replace(',','')
        try:
            test = float(new_population)
        except ValueError:
            QMessageBox.information(self, 'Error', 'You should input valid numeric value!', QMessageBox.Ok)
            # restore to origin number
            currentIndex = self.listWidget_countries.currentRow()
            origin_population = self.countries[currentIndex][1]
            self.textEdit_population.setText(self.thousand_separator(origin_population))
        else:
            # update the country's population
            currentIndex = self.listWidget_countries.currentRow()
            self.countries[currentIndex][1] = new_population
            # renew the screen
            self.display_country_data(currentIndex)
            # there is something changed.
            self.is_changed = True

    def save_changes_to_file(self, file):
        # set Access mode as read only
        WRITE_ACCESS = "w"
        with open(file, WRITE_ACCESS) as countriesFile:
            for country in self.countries:
                countriesFile.write(",".join(country) + "\n")
        # self.exit_application()

    def closeEvent(self, event):

        if self.is_changed:
            quit_msg = "Want to save your changes to the file?"
            reply = QMessageBox.question (self, 'Exit?',
                                         quit_msg, QMessageBox.Yes, QMessageBox.No)

            if reply == QMessageBox.Yes:
                # save the list to the file
                self.save_changes_to_file(self.FILE_PATH)
                event.accept()
            else:
                event.accept()

    def thousand_separator(self, str):
        # apply numeric format on string
        result = str
        str_len = len(result)
        decimal_point=""
        if '.' in result:
            decimal_point = result[str_len-3:]
            result = result[:str_len-3]
            str_len = len(result)

        num_separator = int(str_len/3)

        if str_len%3 == 0:
            num_separator -= 1

        if num_separator > 0:
            location = str_len
            for i in range(num_separator):
                location = len(result) -3*(i+1) -(i)
                result = result[:location]+","+result[location:]

        if decimal_point != "":
            result += decimal_point
        return result

# DO NOT MODIFY THIS CODE
if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_form = MyForm()
    the_form.show()
    sys.exit(app.exec_())
# END DO NOT MODIFY
