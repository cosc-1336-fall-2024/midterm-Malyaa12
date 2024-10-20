#write functions here, don't add input('') statements here!
def get_assessment_value(value):
    return value * 0.60

def get_tax_assessed(assessment_value):
    return (assessment_value / 100) * 0.72

def start_tax_calculation():
    while True:
        try:
            value = float(input("Enter the actual property value: "))
            assessment_value = get_assessment_value(value)
            tax = get_tax_assessed(assessment_value)
            print(f"Assessment Value: {assessment_value:.2f}, Property Tax: {tax:.2f}")
        except ValueError:
            print("Please enter a valid number.")
        
        if input("Do you want to quit? (y/n): ").lower() == 'y':
            break

