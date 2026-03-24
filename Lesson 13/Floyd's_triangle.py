n=int(input("Enter number of rows:"))
num=0
i=0
while i<n:
    x=0
    while x<=i:
        print(num, end="  ")
        x+=1
        num+=1
    i+=1
    print()