#write functions here, don't add input('') statements here!

def get_person_category(age):
    if age < 0:
        return "Invalid number"
    elif age > 125:
        return "Invalid number"
    elif age <= 1:
        return "Infant"
    elif age < 13:
        return "Child"
    elif age < 20:
        return "Teenager"
    else:
        return "Adult"


