# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator_rev01.ui'
#
# Created: Mon Dec 12 20:36:38 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(253, 312)
        self.btn_seven = QtGui.QPushButton(Dialog)
        self.btn_seven.setGeometry(QtCore.QRect(10, 60, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.btn_seven.setFont(font)
        self.btn_seven.setObjectName("btn_seven")
        self.btn_eight = QtGui.QPushButton(Dialog)
        self.btn_eight.setGeometry(QtCore.QRect(70, 60, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.btn_eight.setFont(font)
        self.btn_eight.setObjectName("btn_eight")
        self.btn_nine = QtGui.QPushButton(Dialog)
        self.btn_nine.setGeometry(QtCore.QRect(130, 60, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.btn_nine.setFont(font)
        self.btn_nine.setObjectName("btn_nine")
        self.btn_plus = QtGui.QPushButton(Dialog)
        self.btn_plus.setGeometry(QtCore.QRect(190, 60, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.btn_plus.setFont(font)
        self.btn_plus.setObjectName("btn_plus")
        self.btn_four = QtGui.QPushButton(Dialog)
        self.btn_four.setGeometry(QtCore.QRect(10, 110, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.btn_four.setFont(font)
        self.btn_four.setObjectName("btn_four")
        self.btn_five = QtGui.QPushButton(Dialog)
        self.btn_five.setGeometry(QtCore.QRect(70, 110, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.btn_five.setFont(font)
        self.btn_five.setObjectName("btn_five")
        self.btn_six = QtGui.QPushButton(Dialog)
        self.btn_six.setGeometry(QtCore.QRect(130, 110, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.btn_six.setFont(font)
        self.btn_six.setObjectName("btn_six")
        self.btn_minus = QtGui.QPushButton(Dialog)
        self.btn_minus.setGeometry(QtCore.QRect(190, 110, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.btn_minus.setFont(font)
        self.btn_minus.setObjectName("btn_minus")
        self.btn_one = QtGui.QPushButton(Dialog)
        self.btn_one.setGeometry(QtCore.QRect(10, 160, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.btn_one.setFont(font)
        self.btn_one.setObjectName("btn_one")
        self.btn_two = QtGui.QPushButton(Dialog)
        self.btn_two.setGeometry(QtCore.QRect(70, 160, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.btn_two.setFont(font)
        self.btn_two.setObjectName("btn_two")
        self.btn_three = QtGui.QPushButton(Dialog)
        self.btn_three.setGeometry(QtCore.QRect(130, 160, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.btn_three.setFont(font)
        self.btn_three.setObjectName("btn_three")
        self.btn_multiple = QtGui.QPushButton(Dialog)
        self.btn_multiple.setGeometry(QtCore.QRect(190, 160, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.btn_multiple.setFont(font)
        self.btn_multiple.setObjectName("btn_multiple")
        self.btn_zero = QtGui.QPushButton(Dialog)
        self.btn_zero.setGeometry(QtCore.QRect(10, 210, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.btn_zero.setFont(font)
        self.btn_zero.setObjectName("btn_zero")
        self.btn_clear = QtGui.QPushButton(Dialog)
        self.btn_clear.setGeometry(QtCore.QRect(70, 210, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.btn_clear.setFont(font)
        self.btn_clear.setObjectName("btn_clear")
        self.btn_equal = QtGui.QPushButton(Dialog)
        self.btn_equal.setGeometry(QtCore.QRect(130, 210, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.btn_equal.setFont(font)
        self.btn_equal.setObjectName("btn_equal")
        self.btn_divide = QtGui.QPushButton(Dialog)
        self.btn_divide.setGeometry(QtCore.QRect(190, 210, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.btn_divide.setFont(font)
        self.btn_divide.setObjectName("btn_divide")
        self.lineedit_result = QtGui.QLineEdit(Dialog)
        self.lineedit_result.setGeometry(QtCore.QRect(10, 10, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineedit_result.setFont(font)
        self.lineedit_result.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineedit_result.setObjectName("lineedit_result")
        self.btn_point = QtGui.QPushButton(Dialog)
        self.btn_point.setGeometry(QtCore.QRect(10, 260, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.btn_point.setFont(font)
        self.btn_point.setObjectName("btn_point")
        self.btn_root = QtGui.QPushButton(Dialog)
        self.btn_root.setGeometry(QtCore.QRect(70, 260, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.btn_root.setFont(font)
        self.btn_root.setObjectName("btn_root")
        self.btn_log = QtGui.QPushButton(Dialog)
        self.btn_log.setGeometry(QtCore.QRect(130, 260, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.btn_log.setFont(font)
        self.btn_log.setObjectName("btn_log")
        self.btn_clear_2 = QtGui.QPushButton(Dialog)
        self.btn_clear_2.setGeometry(QtCore.QRect(190, 260, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.btn_clear_2.setFont(font)
        self.btn_clear_2.setObjectName("btn_clear_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Calculator", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_seven.setText(QtGui.QApplication.translate("Dialog", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_eight.setText(QtGui.QApplication.translate("Dialog", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_nine.setText(QtGui.QApplication.translate("Dialog", "9", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_plus.setText(QtGui.QApplication.translate("Dialog", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_four.setText(QtGui.QApplication.translate("Dialog", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_five.setText(QtGui.QApplication.translate("Dialog", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_six.setText(QtGui.QApplication.translate("Dialog", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_minus.setText(QtGui.QApplication.translate("Dialog", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_one.setText(QtGui.QApplication.translate("Dialog", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_two.setText(QtGui.QApplication.translate("Dialog", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_three.setText(QtGui.QApplication.translate("Dialog", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_multiple.setText(QtGui.QApplication.translate("Dialog", "*", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_zero.setText(QtGui.QApplication.translate("Dialog", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_clear.setText(QtGui.QApplication.translate("Dialog", "C", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_equal.setText(QtGui.QApplication.translate("Dialog", "=", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_divide.setText(QtGui.QApplication.translate("Dialog", "/", None, QtGui.QApplication.UnicodeUTF8))
        self.lineedit_result.setPlaceholderText(QtGui.QApplication.translate("Dialog", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_point.setText(QtGui.QApplication.translate("Dialog", ".", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_root.setText(QtGui.QApplication.translate("Dialog", "√", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_log.setText(QtGui.QApplication.translate("Dialog", "log", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_clear_2.setText(QtGui.QApplication.translate("Dialog", "C", None, QtGui.QApplication.UnicodeUTF8))

