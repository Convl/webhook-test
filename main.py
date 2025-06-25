#!/usr/bin/env python3
"""
Calculator CLI Application

A simple command-line calculator that supports basic arithmetic operations.
"""

import calculator


def display_menu():
    """Display the calculator menu."""
    print("\n=== Simple Calculator ===")
    print("Available operations:")
    operations = calculator.get_available_operations()
    for i, op in enumerate(operations, 1):
        print(f"{i}. {op.replace('_', ' ').title()}")
    print("0. Exit")


def get_numbers():
    """Get two numbers from user input."""
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        return a, b
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return None, None


def get_single_number():
    """Get a single number from user input."""
    try:
        a = float(input("Enter number: "))
        return a
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return None


def main():
    """Main calculator loop."""
    print("Welcome to the Simple Calculator!")

    while True:
        display_menu()
        try:
            choice = int(input("\nEnter your choice (0-8): "))
        except ValueError:
            print("Invalid choice. Please enter a number.")
            continue

        if choice == 0:
            print("Thank you for using the calculator!")
            break
        elif choice == 1:  # Add
            a, b = get_numbers()
            if a is not None and b is not None:
                result = calculator.add(a, b)
                print(f"Result: {a} + {b} = {result}")
        elif choice == 2:  # Subtract
            a, b = get_numbers()
            if a is not None and b is not None:
                result = calculator.subtract(a, b)
                print(f"Result: {a} - {b} = {result}")
        elif choice == 3:  # Multiply
            a, b = get_numbers()
            if a is not None and b is not None:
                result = calculator.multiply(a, b)
                print(f"Result: {a} * {b} = {result}")
        elif choice == 4:  # Divide
            a, b = get_numbers()
            if a is not None and b is not None:
                try:
                    result = calculator.divide(a, b)
                    print(f"Result: {a} / {b} = {result}")
                except ValueError as e:
                    print(f"Error: {e}")
        elif choice == 5:  # Power
            a, b = get_numbers()
            if a is not None and b is not None:
                result = calculator.power(a, b)
                print(f"Result: {a} ^ {b} = {result}")
        elif choice == 6:  # Modulus
            a, b = get_numbers()
            if a is not None and b is not None:
                try:
                    result = calculator.modulus(a, b)
                    print(f"Result: {a} % {b} = {result}")
                except ValueError as e:
                    print(f"Error: {e}")
        elif choice == 7:  # Square Root
            a = get_single_number()
            if a is not None:
                try:
                    result = calculator.square_root(a)
                    print(f"Result: √{a} = {result}")
                except ValueError as e:
                    print(f"Error: {e}")
        elif choice == 8:  # Factorial
            a = get_single_number()
            if a is not None:
                try:
                    result = calculator.factorial(a)
                    print(f"Result: {a}! = {result}")
                except ValueError as e:
                    print(f"Error: {e}")
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
