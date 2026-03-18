number=int(input("Enter number:"))
count=0
num=number
for i in range(10):
    if num==i:
        count=1
    else:
        while num!=0:
            num=int(num/10)
            count+=1
print(number,"has",count,"digit/s")