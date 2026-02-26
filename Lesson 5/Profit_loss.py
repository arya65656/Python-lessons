cp= float(input("PLease enter the Cost price:"))
sp= float(input("PLease enter the Selling price:"))
if sp>cp:
    profit= sp-cp
    print("The total profit is:", profit)
else:
    print("No profit")
