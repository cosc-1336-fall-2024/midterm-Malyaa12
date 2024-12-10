#add import
from question_b import get_assessment_value, get_tax_assessed

def main():
    while True:
        try:
            actual_value = float(input("Enter the actual value of the property: "))
            assessment_value = get_assessment_value(actual_value)
            tax = get_tax_assessed(assessment_value)
            print(f"Assessment value: ${assessment_value:.2f}")
            print(f"Property tax: ${tax:.2f}")
        except ValueError:
            print("Please enter a valid number.")
        
        continue_program = input("Do you want to calculate for another property? (yes/no): ").strip().lower()
        if continue_program != 'yes':
            break

if __name__ == "__main__":
    main()
