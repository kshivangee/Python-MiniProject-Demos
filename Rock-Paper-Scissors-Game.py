#Rock-Paper and Scissors

import random
choice = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors"))

computer_choice = random.randint(0,2)

print(choice, computer_choice)

if((choice == 0 and computer_choice==1) or (choice == 0 and computer_choice==2) or(choice==2 and computer_choice==1)):
    print("You win!!!Hurray:)")

elif((choice == 0 and computer_choice==0) or (choice == 1 and computer_choice==1) or (choice == 2 and computer_choice==2)):
    print("It's a draw")
elif((computer_choice == 0 and choice==1) or (computer_choice == 0 and choice==2) or(computer_choice==2 and choice==1)):
    print("Computer win!!!Sad:(")
else:
    print("Game Over!!!  Enter valid number!!!")