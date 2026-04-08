try:
    num1, num2 = eval(input("Enter two numbers separated by a comma: "))
    result = num1 / num2
    print(result)
except ZeroDivisionError:
    print("Division by zero is error !!")
except SyntaxError:
    print("Please enter the numbers in the correct format: 1, 2")
except Exception:
    print("Wrong input")
else:
    print("No exceptions")
finally:
    print("This will execute no matter what")