q = 1
if (type(q) is int):
    print("True")  

w = 1.2345
if (type(w) is not float):
    print("True")
else:
    print("False")

x = 20
y = 20
if (x is y):
    print("x and y have the same identity")

y = 30
if (x is not y):
    print("x and y have different identity")