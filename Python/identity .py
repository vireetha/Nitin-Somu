x = 5
if (type(x) is int):
    print("True")
else:
    print("False")
    
x = 0.5
if(type(x) is not float):
    print("True")
else:
    print("False")
x = 20
y = 20
if ( x is y):
    print("X & Y SAME identity")
y = 30
if ( x is not y):
    print("x & y have different identity")