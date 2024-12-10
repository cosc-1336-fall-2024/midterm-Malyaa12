#add import
from question_d import get_miles_per_hour

def main():
    while True:
        try:
            kilometers = int(input("Enter the distance in kilometers: "))
            minutes = int(input("Enter the time in minutes: "))
            result = get_miles_per_hour(kilometers, minutes)
            if result == "Invalid arguments":
                print(result)
            else:
                print(f"Speed: {result:.6f} miles per hour")
        except ValueError:
            print("Please enter valid numbers.")
        
        continue_program = input("Do you want to calculate another speed? (yes/no): ").strip().lower()
        if continue_program != 'yes':
            break

if __name__ == "__main__":
    main()
