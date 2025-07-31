weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or L): ")

if unit.upper() == "K":
    weight *= 2.205
    print(f"Your weight is: {round(weight, 1)} Lbs.")
elif unit.upper() == "L":
    weight /= 2.205
    print(f"Your weight is: {round(weight, 1)} Kgs.")
else:
    print("Invalid unit")
