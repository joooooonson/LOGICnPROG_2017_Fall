import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap

#ADD IMPORT STATEMENT FOR YOUR GENERATED UI.PY FILE HERE
import spaceview

#CHANGE THE SECOND PARAMETER HERE TO MATCH YOUR GENERATED UI.PY FILE
class MyForm(QMainWindow, spaceview.Ui_MainWindow):
    space1 = "../imgs/space1.jpg"
    space2 = "../imgs/space2.jpg"
    space3 = "../imgs/space3.jpg"
    views = [space1, space2, space3]
    cur_index = 0
        # DO NOT MODIFY THIS CODE
    def __init__(self, parent=None):
        super(MyForm, self).__init__(parent)
        self.setupUi(self)
        # END DO NOT MODIFY

        # ADD SLOTS HERE
        self.next_btn.clicked.connect(self.move_next)
        self.prev_btn.clicked.connect(self.move_prev)

    # ADD SLOT FUNCTIONS HERE
    def move_next(self):
        self.cur_index += 1
        if self.cur_index >= len(self.views):
            self.cur_index = 0
        self.myLabel.setPixmap(QPixmap(self.views[self.cur_index]))

    def move_prev(self):
        self.cur_index -= 1
        if self.cur_index <= 0:
            self.cur_index = len(self.views)-1
        self.myLabel.setPixmap(QPixmap(self.views[self.cur_index]))
    #ADD HELPER FUNCTIONS HERE


# DO NOT MODIFY THIS CODE
if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_form = MyForm()
    the_form.show()
    sys.exit(app.exec_())
# END DO NOT MODIFY
