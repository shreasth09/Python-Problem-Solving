# 💰 Personal Expense Tracker (File-Based CLI)

import os

FILE_NAME = "expenses.txt"


# Add expense
def add_expense():
    amount = input("Enter amount: ")
    category = input("Enter category (Food, Travel, etc.): ")
    date = input("Enter date (DD-MM-YYYY): ")

    with open(FILE_NAME, "a") as f:
        f.write(f"{amount},{category},{date}\n")

    print("✅ Expense added successfully!")


# View all expenses
def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("No expenses found.")
        return

    with open(FILE_NAME, "r") as f:
        lines = f.readlines()

    print("\n📋 All Expenses:")
    for line in lines:
        amount, category, date = line.strip().split(",")
        print(f"Amount: {amount} | Category: {category} | Date: {date}")


# Total expense
def total_expense():
    if not os.path.exists(FILE_NAME):
        print("No expenses found.")
        return

    total = 0
    with open(FILE_NAME, "r") as f:
        for line in f:
            amount = float(line.split(",")[0])
            total += amount

    print("💸 Total Expense:", total)


# Category-wise analysis
def category_analysis():
    if not os.path.exists(FILE_NAME):
        print("No expenses found.")
        return

    data = {}

    with open(FILE_NAME, "r") as f:
        for line in f:
            amount, category, _ = line.strip().split(",")
            amount = float(amount)

            if category in data:
                data[category] += amount
            else:
                data[category] = amount

    print("\n📊 Category-wise Spending:")
    for cat, amt in data.items():
        print(cat, ":", amt)


# Search by date
def search_by_date():
    date = input("Enter date to search: ")

    if not os.path.exists(FILE_NAME):
        print("No expenses found.")
        return

    found = False
    with open(FILE_NAME, "r") as f:
        for line in f:
            if date in line:
                print(line.strip())
                found = True

    if not found:
        print("No records found for this date.")


# Main menu
def main():
    while True:
        print("\n==== EXPENSE TRACKER ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Category Analysis")
        print("5. Search by Date")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            total_expense()

        elif choice == "4":
            category_analysis()

        elif choice == "5":
            search_by_date()

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()