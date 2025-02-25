from datetime import datetime

def menu():
    print("""
        1. Add on expenses
        2. View all expenses
        3. Calculate total expenses
        4. Exit
    """)

def add_expense(date, description, amount):
    try:
        date_object = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid input. No be GADUS BE DIS, enter better date joor")
        return

    try:
        amount = float(amount)
    except ValueError:
        print("Invalid input Gadus. Enter a valid amount")
        return

    expense_tracker.append({"Date": date_object, "Description": description, "Amount": amount})
    print("Expense added successfully!")

def view_expenses():
    if not expense_tracker:
        print("No expenses yet")
        return

    print("Expenses:")
    for expense in expense_tracker:
        print(f"Date: {expense['Date']} \tDescription: {expense['Description']} \tAmount: {expense['Amount']:.2f}")
    print()

def calculate_total_expenses():
    if not expense_tracker:
        print("You haven't bought anything yet!")
        return

    total_amount = sum(expense["Amount"] for expense in expense_tracker)
    print(f"Total amount: {total_amount:.2f}")
    print()

def exit_app():
    print("Exiting the app. Goodbye!")
    exit()

expense_tracker = []
print("Welcome To Semicolon Expense Tracker App")
print("_" * 40)

def main():
    while True:
        menu()
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            # Collect input in main rather than inside the function
            date = input("Enter date (YYYY-MM-DD): ")
            description = input("Enter description: ")
            amount = input("Enter amount: ")
            add_expense(date, description, amount)
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            calculate_total_expenses()
        elif choice == "4":
            exit_app()
        else:
            print("Invalid choice, please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
