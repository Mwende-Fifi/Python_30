"""### Mini Project
Project: Number Guessing Game
Project Description:
The program will randomly select a number between 1 and 100. 
The player will have a limited number of chances (let’s say 7) to guess the number. 
After each guess, the program will tell the player whether their guess is too high or too low. 
If the player guesses correctly within the allowed number of attempts, they win. 
Otherwise, the game ends and the player loses."""

# importing dependencies
import random 

correct_number = random.randint(1, 20)
print("Welcome to the number guessing game")
print("I am thinking a number between 1 and 20.You have 5 attempts to guess it correctly if you win l will give $1000")

attempt = 5

while attempt > 0:

    # collecting numbers
    num = int(input("Please guess the number: "))

    if num == correct_number:
        print("Congrats you won $1000")
    elif num > correct_number:
        print("Your number is too high")
    else:
        print("Your number is too low")

    # reducing the attempt
    attempt -= 1

    print(f"Your attempt left {attempt}")

    if attempt == 0:
        print(f"You're attempt is finished.You lost the game. \nThe correct number was {correct_number}")

    # end