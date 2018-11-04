import sys
import cv2
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot, QSize
import PyQt5.QtGui
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QDialog, QApplication,  QMainWindow
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets
class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        loadUi('g.ui', self)
        self.image= None
        self.loadButton.clicked.connect(self.loadClicked)

    @pyqtSlot()
    def loadClicked(self):
        self.loadImage('t.jpg')
    def loadImage(self, fname):
        self.image= cv2.imread(fname)
        #self.displayImage()
    #def displayImage(self):
        qformat= QImage.Format_Indexed8

        if len(self.image.shape)==3:
            if (self.image.shape[2]==4):
                qformat= QImage.Format_RGBA8888
            else:
                qformat= QImage.Format_RGB888

        img= QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.strides[0], qformat)
        img= img.scaled( self.image.shape[0], self.image.shape[1], 1)
        img= img.rgbSwapped()

        self.imgLabel.setPixmap(QPixmap.fromImage(img))
        self.imgLabel.setAlignment(QtCore.Qt.AlignCenter)


app=QApplication(sys.argv)
window= MyApp()
window.setWindowTitle('My App')
window.show()
sys.exit(app.exec_())
