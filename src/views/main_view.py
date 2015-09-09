'''
Created on Sep 8, 2015

@author: Cassandra
'''
import sys
from PyQt4 import QtGui, uic

class Window(QtGui.QWidget):  #Ventana principal
    def __init__(self):
        uic.loadUi("Space UI.ui",self)
    #   
    def initUI(self):
        self.show()
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()