#coding=gbk
from time import ctime,sleep

def tsfunc(a): #封装带参数的一层
    def daican(func):
        def wrappedFunc():
            print(a)
            print('[%s] %s() called'%(ctime(),func.__name__))
            return func()
        return wrappedFunc
    return daican

@tsfunc('daicanshu')
def test():
    print('test() is running.')

for i in range(2):
    sleep(1)
    test()