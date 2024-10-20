#write functions here, don't add input('') statements here!

def get_person_category(age):
    if age < 0 or age > 125:
        return "Invalid number"
    elif age <= 1:
        return "infant"
    elif age < 13:
        return "child"
    elif age < 20:
        return "teenager"
    else:
        return "adult"

def start_age_classification():
    while True:
        try:
            age = int(input("Enter age: "))
            print(get_person_category(age))
        except ValueError:
            print("Please enter a valid number.")
        
        if input("Do you want to quit? (y/n): ").lower() == 'y':
            break

