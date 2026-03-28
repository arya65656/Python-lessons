row=int(input("Enter number of rows:"))
i=1
num=1
while i<=row:
    print(" "*(row-i)+str(num)*(2*i-1))
    i+=1
    num+=1
i=row-1
num=row-1
while i>0:
    print(" "*(row-i)+str(num)*(2*i-1))
    i-=1
    num-=1


row=int(input("Enter number of rows:"))
i=1
num=1
while i<=row:
    print(" "*(row-i)+str(num)*(2*i-1))
    i+=1
    num+=1
i=row-1
while i>0:
    print(" "*(row-i)+str(num)*(2*i-1))
    i-=1
    num+=1
    
