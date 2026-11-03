from itertools import product
from time import time

letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
special = " !#$%&*/()=?-_"
chars = letters + numbers + special


def crack_password(password, max_length, chars):
    # quick guards: don't brute-force something we already know we can't find
    if len(password) > max_length:
        return False, 0, 0.0
    if any(character not in chars for character in password):
        return False, 0, 0.0

    start = time()
    attempts = 0

    for length in range(1, max_length + 1):
        for combo in product(chars, repeat=length):
            attempts += 1
            if "".join(combo) == password:
                return True, attempts, time() - start

    return False, attempts, time() - start


def get_max_length():
    while True:
        try:
            value = int(input("What is the maximum password length? "))
            if value > 0:
                return value
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Please enter a whole number.")


def show_results(found, password, attempts, runtime):
    if found:
        print(f"\nPassword found: {password!r}")
    else:
        print("\nPassword not found (too long, or it uses characters outside the set).")
    print(f"Attempts: {attempts:,}")
    print(f"Runtime: {runtime:.4f} seconds")


def main():
    print("\n" + "=" * 50)
    print("           PASSWORD TESTER")
    print("=" * 50)

    password = input("Enter your password: ")
    max_length = get_max_length()

    found, attempts, runtime = crack_password(password, max_length, chars)
    show_results(found, password, attempts, runtime)


if __name__ == "__main__":
    main()
