unit = input(
    "What is the unit of measurement you want to convert from? (C = Celsius OR F = Fahrenheit): ")

if unit.upper() not in ['C', 'F']:
    print("Invalid input. Please enter C for Celsius or F for Fahrenheit")
else:
    try:
        temp = float(input("Enter the temperature you want to convert: "))
        if unit.upper() == 'C':
            print(f"{temp}°C is equal to {round(((9 * temp) / 5 + 32), 2)}°F")
        elif unit.upper() == 'F':
            print(f"{temp}°F is equal to {round(((temp - 32) * 5/9), 2)}°C")
    except Exception as ex:
        print(f"An error occurred: {ex}")
