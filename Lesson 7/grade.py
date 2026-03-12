print("Enter Marks Obtained in 5 Subjects out of 100: ")
m1 = int(input("Subject 1: "))
m2 = int(input("Subject 2: "))
m3 = int(input("Subject 3: "))
m4 = int(input("Subject 4: "))
m5 = int(input("Subject 5: "))

tot = m1 + m2+ m3 + m4 + m5
avg = tot/5

print("Total Marks:", tot)
print("Average Mark:", avg)

if 91 <= avg <= 100:
    print("Your Grade is A1")
elif 81 <= avg < 91:
    print("Your Grade is A2")
elif 71 <= avg < 81:
    print("Your Grade is B1")
elif 61 <= avg < 71:
    print("Your Grade is B2")
elif 51 <= avg < 61:
    print("Your Grade is C1")
elif 41 <= avg < 51:
    print("Your Grade is C2")
elif 33 <= avg < 41:
    print("Your Grade is D")
elif 21 <= avg < 33:
    print("Your Grade is E1")
elif 0 <= avg < 21:
    print("Your Grade is E2")
else:
    print("Invalid Input!")