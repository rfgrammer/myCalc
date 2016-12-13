import sys

from PySide.QtCore import *
from PySide.QtGui import *

import showGui


class MainDialog(QDialog, showGui.Ui_Dialog):

    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)

        self.connect(self.btn_one, SIGNAL("clicked()"), self.btn_one_clicked)
        self.connect(self.btn_two, SIGNAL("clicked()"), self.btn_two_clicked)
        self.connect(self.btn_three, SIGNAL("clicked()"), self.btn_three_clicked)
        self.connect(self.btn_four, SIGNAL("clicked()"), self.btn_four_clicked)

        self.connect(self.btn_plus, SIGNAL("clicked()"), self.btn_plus_clicked)
        self.connect(self.btn_minus, SIGNAL("clicked()"), self.btn_minus_clicked)
        self.connect(self.btn_multiple, SIGNAL("clicked()"), self.btn_multiple_clicked)
        self.connect(self.btn_divide, SIGNAL("clicked()"), self.btn_divide_clicked)
        self.connect(self.btn_equal, SIGNAL("clicked()"), self.btn_equal_clicked)
        self.connect(self.btn_clear, SIGNAL("clicked()"), self.btn_clear_clicked)

    def btn_one_clicked(self):
        self.lineedit_result.setText(self.lineedit_result.text() + '1')

    def btn_two_clicked(self):
        self.lineedit_result.setText(self.lineedit_result.text() + '2')

    def btn_three_clicked(self):
        self.lineedit_result.setText(self.lineedit_result.text() + '3')

    def btn_four_clicked(self):
        self.lineedit_result.setText(self.lineedit_result.text() + '4')

    def btn_five_clicked(self):
        self.lineedit_result.setText(self.lineedit_result.text() + '5')

    def btn_six_clicked(self):
        self.lineedit_result.setText(self.lineedit_result.text() + '6')

    def btn_seven_clicked(self):
        self.lineedit_result.setText(self.lineedit_result.text() + '7')

    def btn_eight_clicked(self):
        self.lineedit_result.setText(self.lineedit_result.text() + '8')

    def btn_nine_clicked(self):
        self.lineedit_result.setText(self.lineedit_result.text() + '9')

    def btn_plus_clicked(self):
        self.lineedit_result.setText(self.lineedit_result.text() + '+')

    def btn_minus_clicked(self):
        self.lineedit_result.setText(self.lineedit_result.text() + '-')

    def btn_multiple_clicked(self):
        self.lineedit_result.setText(self.lineedit_result.text() + '*')

    def btn_divide_clicked(self):
        self.lineedit_result.setText(self.lineedit_result.text() + '/')

    def btn_clear_clicked(self):
        self.lineedit_result.clear()

    def btn_equal_clicked(self):
        try:
            self.lineedit_result.setText(str(eval(self.lineedit_result.text())))
        except Exception, e:
            QMessageBox.show(e.message)


def main():
    app = QApplication(sys.argv)
    form = MainDialog()
    form.show()
    app.exec_()


if __name__ == "__main__":
    main()