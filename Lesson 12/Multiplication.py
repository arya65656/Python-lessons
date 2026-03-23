num = input("Enter a number: ")
numlen = len(num)

if numlen % 2 == 1: 
    midl1 = numlen // 2
    midl2 = midl1
    output = int(num[midl1])
else: 
    midl1 = numlen // 2 - 1
    midl2 = midl1 + 1
    output = int(num[midl1]) * int(num[midl2])

print(f"The product of the middle digit/s is {output}")
