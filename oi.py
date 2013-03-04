from threading import Thread
from subprocess import *
import os
import sqlite3

from PyQt4.QtCore import *
from PyQt4.QtGui import *


class OI_GUI(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.create_main_frame()       

    def create_main_frame(self):        
        page = QWidget()        

        self.edit1 = QTextEdit()
        self.button = QPushButton('joy', page)

        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.edit1)
        vbox1.addWidget(self.button)
        page.setLayout(vbox1)
        self.setCentralWidget(page)

        self.connect(self.button, SIGNAL("clicked()"), self.clicked)

    def clicked(self):
        QMessageBox.about(self, "My message box", "Text1 = %s" % self.edit1.toPlainText())



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    form = OI_GUI()
    form.show()
    app.exec_()
