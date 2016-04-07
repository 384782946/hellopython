
class A(): pass

class B(A): pass

def test():
    a = A()
    b = B()
    print("type of A:",type(A))
    print("type of a:",type(a))
    print("type of B:",type(B))
    print("type of b:",type(b))
    #x=input('please input a var:')
    #print(type(x),x)
    
    print("a isinstance (A,B):",isinstance(a, (A,B)))
    print("1 isinstance (A,B):",isinstance(1, (A,B)))

if __name__ == "__main__":
    #test()
    print(type(1.1))