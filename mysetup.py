from distutils.core import setup
import py2exe

#setup(windows=['videoCapture.py'],options={"py2exe":{"includes":["sip","VideoCapture", "PyQt4.QtGui"]}})
#setup(windows=['genQRCode.py'], options={"py2exe": {"includes": ["qrcode","sip", "PyQt4.QtGui"]}})

op={"py2exe": {"includes": ["requests.exceptions"]}}

setup(console=['weixin.py'] , options=op)