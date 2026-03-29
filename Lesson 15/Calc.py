def add(p,q):
    return(p+q)
def sub(p,q):
    return(p-q)
def mul(p,q):
    return(p*q)
def div(p,q):
    if q==0:
        return("Error: Cannot divide with 0")
    else:
        return(p/q)
def sqr(p,q):
    return(p**q)
def root(p,q):
    return(p**0.5,q**0.5)
print("Select operation:")
print("a) ADD")
print("b) SUBTRACT")
print("c) MULTIPLY")
print("d) DIVIDE")
print("d) SQUARE")
print("f) SQUARE ROOT")
choice=(input("Enter one operation: "))
p = float(input("Enter first number: "))
q = float(input("Enter second number: "))
if choice == 'a':
    print("Result:", add(p,q))
elif choice == 'b':
    print("Result:", sub(p,q))
elif choice == 'c':
    print("Result:", mul(p,q))
elif choice == 'd':
    print("Result:", div(p,q))
elif choice == 'e':
    print("Result:", sqr(p,q))
elif choice == 'f':
    print("Result:", root(p,q))
else:
    print("Invalid choice")