"this is a test com moule"
import win32com.client as win32
from time import sleep
import win32com
from win32com.client import Dispatch,constants

def test_excel():
    "this is a function for test excel programing."
    excel = win32.Dispatch('Excel.Application')
    ss = excel.Workbooks.Add()
    sh = ss.ActiveSheet
    excel.Visible = False
    sleep(1)
    sh.Cells(1,1).Value = 'Python-to-%s Demo' % 'Excel'
    sleep(1)
    for i in range(3,8):
        sh.Cells(i,1).Value = 'Line %d' % i
        sleep(1)
    
    sleep(10)
    ss.Close(True)
    excel.Application.Quit()

def test_word():
    word = win32.Dispatch('Word.Application')
    doc = word.Documents.Add()
    #doc = word.Documents.Open(r'D\a.doc')
    word.Visible = True
    sleep(1)

    rng = doc.Range(0,0)
    #rng.InsertAfter('Python-to-Word\r\n')
    #wordSlct = rng.Select()
    #wordSlct.Style = constants.wdStyleHeading1
    
    sleep(1)
    doc.Tables.Add(rng,3,3)
    table = doc.Tables[0]
    for i in range(1,4):
        for j in range(1,4):
            table.Cell(i,j).Range.Text = "cell %d,%d" %(i,j)
            
#     for i in range(3,8):
#         rng.InsertAfter('Line %d\r\n' % i)
#         sleep(1)
    
#     rng.InsertAfter("\r\nTh-th-th-that's all folks!\r\n")
    doc.Close(True)
    word.Application.Quit()

#test_excel()
test_word()