#coding=gbk
import qrcode
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
import sys
from PyQt4.Qt import QSize, QPixmap

class MyDialog(QtGui.QDialog):
    '''主窗口'''
    def __init__(self):
        super(MyDialog,self).__init__()
        self.setWindowTitle("QRCodeGenerator")
        self.editText = QtGui.QLineEdit()
        self.imgLabel = QtGui.QLabel()
        self.btn = QPushButton("Gen")
        self.btn.clicked.connect(self.btn_clicked)
        hBoxLayout = QHBoxLayout()
        hBoxLayout.addWidget(self.editText)
        hBoxLayout.addWidget(self.btn)
        self.rootLayout = QVBoxLayout()
        self.rootLayout.addLayout(hBoxLayout)
        self.rootLayout.addWidget(self.imgLabel)
        self.setLayout(self.rootLayout)
        self.resize(QSize(300,350))
    
    def gen(self,txt):
        qr = qrcode.QRCode(version=2,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=1)
        qr.add_data(txt)
        qr.make(fit=True)
        img = qr.make_image()
        name = "qrcode_tmp.png"
        img.save(name, "png")
        return name

    def btn_clicked(self):
        txt = self.editText.text()
        fileName = self.gen(txt)
        self.imgLabel.setPixmap(QPixmap(fileName))
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = MyDialog()
    dlg.show()
    app.exec_()