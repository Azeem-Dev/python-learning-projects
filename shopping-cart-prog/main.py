

foods = []
prices = []

total = 0

while True:
    food = input("Enter the name of the food (q to quit): ")
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print("----- YOUR CART -----")


"""THE BELOW IS THE WAY WE CAN ITERATE OVER MAIN LIST GET INDEX AND THEN USE THAT INDEX TO GET THE PRICE FROM THE PRICES LIST"""
# for food in foods:
#     print(f"{food}: ${prices[foods.index(food)]}", end=" | ")

for index, food in enumerate(foods):
    if (index == len(foods)-1):
        print(f"{food}: ${prices[index]}")
    else:
        print(f"{food}: ${prices[index]}", end=" | ")


total = 0
[total := total + price for price in prices]

print(f"Your total is ${total}")
