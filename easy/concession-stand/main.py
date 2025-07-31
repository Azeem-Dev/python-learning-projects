

menu = {
    "pizza": 3.00,
    "nachos": 4.50,
    "popcorn": 6.00,
    "fries": 2.50,
    "chips": 1.00,
    "pretzel": 3.50,
    "soda": 3.00,
    "lemonade": 4.25,
}


cart = []
total = 0.0

print("----------------- MENU -------------------")
for key, value in menu.items():
    print(f"{key}: ${value:.2f}")
print("------------------------------------------")


while True:
    food = input("Select an item (q to quit): ")
    if food.lower() == 'q':
        break
    elif menu.get(food) is not None:
        cart.append(food)
    else:
        print(f"Sorry, {food} is not on the menu.\n")

print("-----------YOUR ORDER-----------")

for index, food in enumerate(cart):
    total += menu.get(food)
    if index != len(cart) - 1:
        print(food, end=" | ")
    else:
        print(food)


print(f"Your total is: ${total:.2f}")
