import math


def checkPrimeNumber(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    isPrime = True

    for divisor in range(3, n, 2):
        if n % divisor == 0:
            isPrime = False
            break

    return isPrime


if __name__ == "__main__":
    number = int(input("Please enter a number to check prime: "))
    if checkPrimeNumber(number):
        print(f"The number {number} is a prime number")
    else:
        print(f"The number {number} is not a prime number")
