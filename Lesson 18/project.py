try:
    age = int(input("Enter your age: "))
    if age % 2 == 0:
        print("Even")
    else:
        print("Odd")
except ValueError:
    print("Value error: Please enter a whole number (no decimals, letters, or symbols).")