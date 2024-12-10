#add import
from question_a import get_random_number

def main():
    while True:
        target_number = get_random_number()
        print("Guess the number (between 1 and 5):")
        while True:
            try:
                guess = int(input("Your guess: "))
                if guess == target_number:
                    print("Congratulations! You guessed it right!")
                    break
                else:
                    print("Wrong guess, try again!")
            except ValueError:
                print("Please enter a valid number.")
        
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
