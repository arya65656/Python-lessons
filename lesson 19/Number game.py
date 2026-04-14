import random
number=str(random.randint(0,9))
playing= True
print("Guess the number between 0 and 9")
while playing:
    guess=input("Your guess: ")
    if number==guess:
        print("You got it right! The number was", number)
        break
    print("Try again.")
