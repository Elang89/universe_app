# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_view.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(948, 638)
        MainWindow.setMinimumSize(QtCore.QSize(948, 638))
        MainWindow.setMaximumSize(QtCore.QSize(948, 638))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.events = QtGui.QComboBox(self.centralwidget)
        self.events.setGeometry(QtCore.QRect(690, 190, 111, 22))
        self.events.setEditable(False)
        self.events.setObjectName(_fromUtf8("events"))
        self.events.addItem(_fromUtf8(""))
        self.events.addItem(_fromUtf8(""))
        self.events.addItem(_fromUtf8(""))
        self.events.addItem(_fromUtf8(""))
        self.events.addItem(_fromUtf8(""))
        self.comboBox_4 = QtGui.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(810, 190, 111, 22))
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.new_event_button = QtGui.QPushButton(self.centralwidget)
        self.new_event_button.setGeometry(QtCore.QRect(690, 220, 111, 23))
        self.new_event_button.setMouseTracking(False)
        self.new_event_button.setAccessibleName(_fromUtf8(""))
        self.new_event_button.setAutoFillBackground(False)
        self.new_event_button.setAutoRepeat(False)
        self.new_event_button.setAutoDefault(False)
        self.new_event_button.setDefault(False)
        self.new_event_button.setFlat(False)
        self.new_event_button.setObjectName(_fromUtf8("new_event_button"))
        self.search_event_button = QtGui.QPushButton(self.centralwidget)
        self.search_event_button.setGeometry(QtCore.QRect(810, 220, 111, 23))
        self.search_event_button.setObjectName(_fromUtf8("search_event_button"))
        self.delete_event_button = QtGui.QPushButton(self.centralwidget)
        self.delete_event_button.setGeometry(QtCore.QRect(690, 250, 111, 23))
        self.delete_event_button.setObjectName(_fromUtf8("delete_event_button"))
        self.edit_event_button = QtGui.QPushButton(self.centralwidget)
        self.edit_event_button.setGeometry(QtCore.QRect(810, 250, 111, 23))
        self.edit_event_button.setObjectName(_fromUtf8("edit_event_button"))
        self.show_table = QtGui.QTableWidget(self.centralwidget)
        self.show_table.setGeometry(QtCore.QRect(20, 20, 651, 581))
        self.show_table.setObjectName(_fromUtf8("show_table"))
        self.show_table.setColumnCount(0)
        self.show_table.setRowCount(0)
        self.new_event_button_2 = QtGui.QPushButton(self.centralwidget)
        self.new_event_button_2.setGeometry(QtCore.QRect(710, 360, 201, 23))
        self.new_event_button_2.setObjectName(_fromUtf8("new_event_button_2"))
        self.new_event_button_3 = QtGui.QPushButton(self.centralwidget)
        self.new_event_button_3.setGeometry(QtCore.QRect(710, 390, 201, 23))
        self.new_event_button_3.setObjectName(_fromUtf8("new_event_button_3"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 948, 18))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Universe Galaxies", None))
        self.events.setItemText(0, _translate("MainWindow", "Galactic Events", None))
        self.events.setItemText(1, _translate("MainWindow", "PLanetary Event", None))
        self.events.setItemText(2, _translate("MainWindow", "Asteroid Impacts", None))
        self.events.setItemText(3, _translate("MainWindow", "Nebula Events", None))
        self.events.setItemText(4, _translate("MainWindow", "Stellar Event", None))
        self.new_event_button.setText(_translate("MainWindow", "New Event", None))
        self.search_event_button.setText(_translate("MainWindow", "Search Events", None))
        self.delete_event_button.setText(_translate("MainWindow", "Delete Event", None))
        self.edit_event_button.setText(_translate("MainWindow", "Edit Event", None))
        self.new_event_button_2.setText(_translate("MainWindow", "View Images", None))
        self.new_event_button_3.setText(_translate("MainWindow", "Add Image", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

