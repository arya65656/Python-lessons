import random
while True:
    user_input=input("Enter a choice(rock/paper/scissors): ")
    pa="rock", "paper", "scissors"
    i=(random.choice(pa))
    print("Bot chose: ",i)
    print("You chose:", user_input)
    if user_input=="rock":
        if i=="paper":
            print("You lose!:(") 
        elif i=="scissors":
            print("You win!:)")
        else:
            print("It is a tie...")
    elif user_input=="paper":
        if i=="scissors":
            print("You lose!:(") 
        elif i=="rock":
            print("You win!:)")
        else:
            print("It is a tie...")
    elif user_input=="scissors":
        if i=="rock":
            print("You lose!:(") 
        elif i=="paper":
            print("You win!:)")
        else:
            print("It is a tie...")
    else:
        print("Invalid input! Try again")
    if input("PLAY AGAIN? (Y/N)")!="Y":
        break