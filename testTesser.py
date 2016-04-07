#coding=gbk
from pytesser import *
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
import sys
from PyQt4.Qt import QSize, QPixmap
from PyQt4.QtCore import QString

class MyDialog(QtGui.QDialog):
    '''主窗口'''
    def __init__(self):
        super(MyDialog,self).__init__()
        self.setWindowTitle("ORC")
        self.editText = QtGui.QLineEdit()
        self.imgLabel = QtGui.QLabel()
        self.btn = QPushButton("Image File")
        self.btn.clicked.connect(self.btn_clicked)
        hBoxLayout = QHBoxLayout()
        hBoxLayout.addWidget(self.editText)
        hBoxLayout.addWidget(self.btn)
        self.rootLayout = QVBoxLayout()
        self.rootLayout.addLayout(hBoxLayout)
        self.rootLayout.addWidget(self.imgLabel)
        self.setLayout(self.rootLayout)
        self.resize(QSize(300,350))

    def btn_clicked(self):
        imgPath = QFileDialog.getOpenFileName(parent=self, caption=QString("Select one image file"))
        #image = Image.open(str(imgPath)) # Open image object using PIL
        #retStr = image_to_string(image) # Run tesseract.exe on image fnord
        retStr = image_file_to_string(str(imgPath))
        print retStr
        self.editText.setText(retStr)
        self.imgLabel.setPixmap(QPixmap(imgPath))
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = MyDialog()
    dlg.show()
    app.exec_()