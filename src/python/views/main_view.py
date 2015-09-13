'''
Created on Sep 8, 2015

@author: Cassandra
'''
import sys
from PyQt4 import QtGui
from PyQt4.uic.Compiler.qtproxies import QtCore

class Window(QtGui.QWidget):  #Ventana principal
    def __init__(self):
        super(Window, self).__init__()
        self.initUI()
    #   
    def initUI(self):
        self.events_table = QtGui.QTableWidget()
        self.event_type_selector = QtGui.QComboBox()
        self.event_type_selector.addItem("Galactic Events")
        self.event_type_selector.addItem("Stellar Event")
        self.event_type_selector.addItem("Planetary Event")
        self.event_type_selector.addItem("Asteroid Impacts")
        self.event_type_selector.addItem("Nebula Events")
        self.event_selector = QtGui.QComboBox()
        self.button_new = QtGui.QPushButton("New Event")
        self.button_delete = QtGui.QPushButton("Delete Event")
        self.button_update = QtGui.QPushButton("Edit Event")
        self.button_search = QtGui.QPushButton("Search Events")
        self.button_view_image = QtGui.QPushButton("View Images")
        self.button_add_image = QtGui.QPushButton("Add Image")
        
        self.main_layout = QtGui.QHBoxLayout()
        self.vbox_right = QtGui.QVBoxLayout()
        self.hbox_top_right = QtGui.QHBoxLayout()
        self.vbox_bottom_right = QtGui.QVBoxLayout()   
        self.inner_vbox_1 = QtGui.QVBoxLayout()
        self.inner_vbox_2 = QtGui.QVBoxLayout()
        self.inner_vbox_1.addWidget(self.event_type_selector)
        self.inner_vbox_1.addWidget(self.button_new)
        self.inner_vbox_1.addWidget(self.button_delete)
        self.inner_vbox_2.addWidget(self.event_selector)
        self.inner_vbox_2.addWidget(self.button_search)
        self.inner_vbox_2.addWidget(self.button_update)
        self.hbox_top_right.addLayout(self.inner_vbox_1)
        self.hbox_top_right.addLayout(self.inner_vbox_2)
        self.vbox_bottom_right.addWidget(self.button_view_image)
        self.vbox_bottom_right.addWidget(self.button_add_image)
        self.vbox_right.addLayout(self.hbox_top_right)
        self.vbox_right.addLayout(self.vbox_bottom_right)
        self.main_layout.addWidget(self.events_table)
        self.main_layout.addLayout(self.vbox_right)
        self.setLayout(self.main_layout)
        self.setGeometry(400,400,1280,720)
        self.show()
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()