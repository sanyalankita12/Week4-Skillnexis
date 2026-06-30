# Building calculator using simple functions

def addition():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
    except ValueError:
        print("Please enter valid integers.")
        return
    print(f"Addition of {a} and {b} is {a+b}")

def subtraction():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
    except ValueError:
        print("Please enter valid integers.")
        return
    print(f"Subtraction of {a} and {b} is {a-b}")

def multiplication():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
    except ValueError:
        print("Please enter valid integers.")
        return
    print(f"Multiplication of {a} and {b} is {a*b}")

def division():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
    except ValueError:
        print("Please enter valid integers.")
        return
    if b == 0:
        print("Division by zero is not allowed.")
    else:
        print(f"Division of {a} and {b} is {a / b}")

def menu():
    while True:
        print("=" * 35)
        print("      CALCULATOR")
        print("=" * 35)
        print("1. Addition(+)")
        print("2. Subtraction(-)")
        print("3. Multiplication(*)")
        print("4. Division(/)")
        print("5. Exit")

        try:
            choice = int(input("\nEnter your choice (1-5): "))
        except ValueError:
            print("Please enter a valid number.\n")
            continue

        if choice == 1:
            addition()

        elif choice == 2:
            subtraction()

        elif choice == 3:
            multiplication()

        elif choice == 4:
            division()

        elif choice == 5:
            break

        else:
            print("Invalid choice! Please try again.\n")


menu()