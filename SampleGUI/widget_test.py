## widget_test.py
##
## Asis A Sotelo
## January 20, 2021
##
## A Template for Widget Tests
##


import sys 
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as gtg
from PyQt5 import QtCore as qtc

class MainWindow(qtw.QWidget):
	def __init__(self):
		"""MainWindow Constructor"""

		super().__init__()
		# MAIN UI CODE GOES HERE
	
		# END MAIN UI CODE
		
		self.show()



if __name__=='__main__':
	app = qtw.QApplication(sys.argv)
	mw = MainWindow()
	sys.exit(app.exec())
