a=int(input("Enter speed in km/h for cyclist 1: "))
s=int(input("Enter speed in km/h for cyclist 2: "))
d=int(input("Enter speed in km/h for cyclist 3: "))
avg= (a+s+d)/3
print("The average speed is",avg)
if avg>a:
    print("Cyclist 1 is slower than the average speed")
else:
    print("Cyclist 1 is at or faster than the average speed")
if avg>s:
    print("Cyclist 2 is slower than the average speed")
else:
    print("Cyclist 2 is  at or faster than the average speed")
if avg>d:
    print("Cyclist 3 is slower than the average speed")
else:
    print("Cyclist 3 is at or faster than the average speed")