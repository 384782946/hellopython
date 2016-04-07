#coding=gbk
import VideoCapture
from VideoCapture import Device
from PyQt4.QtGui import *
from PyQt4.Qt import QSize, QPixmap
import sys

cam = Device()

class MyDialog(QDialog):
    def __init__(self):
        super(MyDialog,self).__init__()
        self.setWindowTitle("VideoCapture")
        self.rootLayout = QVBoxLayout()
        self.imgLabel = QLabel()
        self.rootLayout.addWidget(self.imgLabel)
        self.setLayout(self.rootLayout)
        self.startTimer(10)
        self.cam = Device()
    
    def timerEvent(self, *args, **kwargs):
        cam.saveSnapshot('VideoCapture.jpg')
        self.imgLabel.setPixmap(QPixmap("VideoCapture.jpg"))
        return QDialog.timerEvent(self, *args, **kwargs)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = MyDialog()
    dlg.show()
    app.exec_()