#this code is a fun number guessing game. The user will try to guessa randomly generated number betwwen 1 and 50 where they have hints if they guess a higher number or a lower number. 
#They get 10 attempts to guess this number

import random
import time

def number_guess():
    num_to_guess = random.randint(1, 50)
    attempts = 10

    print("Welcome to the number guessing game!")
    #time.sleep(3)
    print("Guess a number between 1 and 50. You have 10 attempts to guess this number.")
    #time.sleep(2)

    num = int(input("Enter your guess: "))
    #time.sleep(2)
    while attempts > 0:
        if num > num_to_guess:
            #time.sleep(1)
            print("Too high!")
        elif num < num_to_guess:
            #time.sleep(1)
            print("Too low!")
        else:
            print("Congratulations, you've guessed the number!")
            break
        attempts -= 1
        num = int(input("Enter your new guess: "))
    #time.sleep(2)
    print("Sorry, you've reached the maximum number of attempts. The number was:", num_to_guess)

number_guess()