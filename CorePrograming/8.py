def test():
    '''test for range:'''
    print(test.__doc__)
    print(list(range(0,10)))
    print(list(range(3,19,3)))
    print(list(range(-20,900,220)))
    
def isSuShu(num):
    return len([i for i in range(2,num) if num%i == 0]) == 0
    
if __name__ == "__main__":
    test()
    for i in range(3,20):
        print(i,":",isSuShu(i))