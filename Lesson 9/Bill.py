z= int(input("Please enter number of units consumed:"))
if z>50:
    amount=(z*2.6)
    charges=25
elif z<=100:
    amount=130+(z-50)*3.25
    charges=35
elif z<=200:
    amount=130+162.5+(z-100)*5.26
    charges=45
else:
    amount=130+162.5+526+(z-200)*8.45
    charges=45
tot=amount+charges
print("Electricity bill is:",round(tot,2))