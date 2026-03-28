# 🧮 CLI Calculator

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b


def main():
    while True:
        print("\n==== CALCULATOR ====")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "5":
            print("Exiting...")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue

        if choice == "1":
            print("Result:", add(a, b))

        elif choice == "2":
            print("Result:", subtract(a, b))

        elif choice == "3":
            print("Result:", multiply(a, b))

        elif choice == "4":
            print("Result:", divide(a, b))


if __name__ == "__main__":
    main()