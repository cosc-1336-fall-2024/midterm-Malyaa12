#write functions here, don't add input('') statements here!

import random

def get_random_number():
    return random.randint(1, 5)

def start_game():
    while True:
        number = get_random_number()
        while True:
            try:
                guess = int(input("Guess the number (1-5): "))
                if guess == number:
                    print("Congratulations! You guessed it!")
                    break
                else:
                    print("Try again!")
            except ValueError:
                print("Please enter a valid number.")
        
        if input("Do you want to quit? (y/n): ").lower() == 'y':
            break

