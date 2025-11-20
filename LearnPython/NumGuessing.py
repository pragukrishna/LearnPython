import random
import time

def number_guess():
    num_to_guess = random.randint(1, 20)

    print("Welcome to the number guessing game!")
    time.sleep(3)
    print("Guess a number between 1 and 20...")
    time.sleep(2)

    num = int(input("Enter your guess: "))
    time.sleep(2)
    while num != num_to_guess:
        if num > num_to_guess:
            time.sleep(1)
            print("Too high!")
        else:
            time.sleep(1)
            print("Too low!")
        num = int(input("Enter your new guess: "))
        time.sleep(2)
    print("Congratulations, you've guessed the number!")

number_guess()