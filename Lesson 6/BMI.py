h=float(input("Enter height in meters:"))
w=float(input("Enter weight in kilograms:"))
bmi=w/(h**2)
print("Your BMI is ", bmi)
if bmi<=18.4:
    print("This person is underweight")
elif bmi<=24.9:
    print("This person is healthy")
elif bmi<=29.9:
    print("This person is overweight")
elif bmi<=34.9:
    print("This person is severly overweight")
elif bmi<=39.9:
    print("This person is obese")
else:
    print("This person is severly obese")
