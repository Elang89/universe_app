import sys
from views import main_view2
from PyQt4.Qt import QApplication, QMainWindow
from data import galaxy

class MainDialog (QMainWindow, main_view2.Ui_MainWindow):
    
    def __init__(self, parent=None):
        super (MainDialog, self).__init__(parent)
        self.setupUi(self)
        self.events.currentIndexChanged.connect(self.slot1)

        

    def slot1 (self):
     

        print (self.events.currentIndex())
        x = galaxy.Galaxy()
        print x.show("")[1]
        
    

        
app = QApplication(sys.argv)
form = MainDialog()
form.show()
app.exec_()