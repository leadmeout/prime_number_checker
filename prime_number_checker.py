def prime_checker(number):

    if number == 1 or number == 2 or number == 3:
        print(f"The number {number} is a prime number.")
    elif number % 2 == 0 or number % 3 == 0:
        print(f"The number {number} is not a prime number.")
    else:
        print(f"The number {number} is a prime number.")


n = int(input("Check this number: "))

prime_checker(number=n)