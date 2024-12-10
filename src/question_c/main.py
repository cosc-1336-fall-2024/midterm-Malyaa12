#add import
from question_c import get_person_category

def main():
    while True:
        try:
            age = int(input("Enter a person's age: "))
            category = get_person_category(age)
            print(f"Category: {category}")
        except ValueError:
            print("Please enter a valid number.")
        
        continue_program = input("Do you want to check another age? (yes/no): ").strip().lower()
        if continue_program != 'yes':
            break

if __name__ == "__main__":
    main()
