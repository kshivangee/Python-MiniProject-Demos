#Guess Number Game Program

import random
def guessgame(chances,number):
    print(f"You have {chances} attempts remaining to guess the number.")
    while(chances>0):
        chances-=1
        guess = int(input("Make a guess: "))
        if(guess>number):
            print("Too high.")
            print("Guess again.")
            print(f"You have {chances} attempt/s remaining to guess the number.")
        elif(guess<number):
            print("Too low.")
            print("Guess again.")
            print(f"You have {chances} attempt/s remaining to guess the number.")
        elif(guess==number):
            print(f"You got it! The answer was {number}")
            break
    if(chances==0 and guess!=number):
        print("You've run out of guesses, you lose.")
    
print("Number Guessing Game")
print("Welcome to the number guessing game!!!")
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty: Type 'easy' or 'hard': ")
number = random.randint(1,100)
#print(f"Guess number: {number}")
if(level == 'easy'):
    guessgame(10, number)
        
if(level == 'hard'):
    guessgame(5, number)
