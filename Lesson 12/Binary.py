num=int(input("Enter a decimal number:"))
bn=" "
if num==0:
    bn="0"
else:
    while num>0:
        r=num%2
        bn=str(r)+bn
        num=num//2
print("Binary conversion is:",bn)
