"""
FORMULA:

A = P (1 + r/n)**t

WHERE:

A = final amount
P = initial amount (principal)
r = annual interest rate (in decimal)
t = time the money is invested for (in years)


"""


principle = 0
rate = 0
time = 0


while True:
    principle = float(input("Enter the principal amount: "))
    if principle <= 0:
        print("Principal can't be less than or equal to zero")
    else:
        break


while True:
    rate = float(input("Enter the interest rate: "))
    if rate <= 0:
        print("Interest rate can't be less than or equal to zero")
    else:
        break


while True:
    time = int(input("Enter the time in years: "))
    if time <= 0:
        print("Time can't be less than or equal to zero")
    else:
        break

total = principle * pow((1 + rate / 100), time)

print(f"Balance after {time} years/s: ${total:.2f}")
