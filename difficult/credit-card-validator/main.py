"""

CREDIT CARD VALIDATOR PROGRAM


1. Remove any '-' or ' '
2. Add all digits in the odd places from right to left
3. Double every second digit from right to left.
    (if result is a two digit number,
    add the two-digit number together to get a single digit.)
4. Sum the totals of steps 2 & 3
5. If sum is divisible by 10, the card number is valid.

"""


sum_odd_digits = 0
sum_even_digits = 0
total = 0

# STEP 1

card_number = input("Enter a credit card #: ")
card_number = card_number.replace("-", "").replace(" ", "")[::-1]

# STEP 2

for x in card_number[::2]:
    sum_odd_digits += int(x)

# STEP 3
for x in card_number[1::2]:
    # print(f"x at the start of for loop : {x}")
    x = int(x) * 2
    if (x >= 10):
        # print(f"x after making it double: {x}", f"mod of x by 10: {x % 10}")
        # HERE AS: THE MAX A NUMBER CAN GO IS 9 and it's double is 18 and if we do 18 % 10 we get 8 so we add 1 to get 9
        sum_even_digits += (1+(x % 10))
    else:
        sum_even_digits += x

# STEP 4
total = sum_odd_digits + sum_even_digits

# STEP 5
if (total % 10 == 0):
    print("Card number is valid.")
else:
    print("Card number is not valid.")
