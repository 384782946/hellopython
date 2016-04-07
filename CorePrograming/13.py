#coding:utf-8
'''
Created on 2016/3/13

@author: zxj
'''

# class MyClass(object):
#     'MyClass class definition'
#     myVersion = '1.1'
#     def showVersion(self):
#         print MyClass.myVersion
#         
# obj = MyClass()
# obj.showVersion()
# 
# print 'dir():',dir(MyClass)
# print '__dict__:',MyClass.__dict__
# print "__module:",MyClass.__module__
# 
# MyClass.myVersion = '1.2'
# print obj.showVersion()
# obj2 = MyClass()
# print obj2.showVersion()

class parentA:
    'parentA class'
    def __init__(self):
        print 'parentA init is called.'
        
class parentB:
    def __init__(self):
        print 'parentB init is called.'
        
class child(parentA,parentB):
    'child class'
    def __init__(self):
        super(child,self).__init__()
        print 'child init is callid.'

obj = child()