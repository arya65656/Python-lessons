import string 

let=input("Enter a character: ")

if len(let) != 1:
    print("Enter one character only.")
elif let in string.ascii_letters:
    print("This is an English alphabet.")
else:
    print("Not an English alphabet.")