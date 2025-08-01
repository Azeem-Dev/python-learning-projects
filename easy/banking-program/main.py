def show_balance(balance):
    print(f"Your current balance is: ${balance:.2f}")


def deposit():
    amount = float(input("Enter an amount to be deposited: "))

    if amount < 0:
        print("Invalid amount. Please enter a positive number.")
        return 0
    else:
        return amount


def withdraw():
    amount = float(input("Enter amount to be withdrawn: "))
    if amount > balance:
        print("Insufficient funds")
        return 0
    elif amount < 0:
        print("Invalid amount. Please enter a positive number.")
        return 0
    else:
        return amount


def main():

    balance = 0
    is_running = True

    while is_running:
        print("Banking Program")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw()
        elif choice == '4':
            is_running = False
        else:
            print("Invalid choice. Please choose a valid option.")

    print("Thank you! have a nice day!")


if __name__ == '__main__':
    main()
