#write functions here, don't add input('') statements here!

def get_miles_per_hour(kilometers, minutes):
    if kilometers < 0 or minutes <= 0:
        return 'Invalid arguments'
    return (kilometers * 0.621371) / (minutes / 60)

def start_speed_conversion():
    while True:
        try:
            kilometers = int(input("Enter kilometers: "))
            minutes = int(input("Enter minutes: "))
            print(f"Miles per hour: {get_miles_per_hour(kilometers, minutes):.2f}")
        except ValueError:
            print("Please enter valid numbers.")
        
        if input("Do you want to quit? (y/n): ").lower() == 'y':
            break
