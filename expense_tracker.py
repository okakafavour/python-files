from datetime import datetime
expense_tracker = []
print("Welcome To Semicolon Expense Tracker App")
print("_" * 40)

def menu():
    print("""
		1. Add on expenses
		2. View all expenses
		3. Calculate total expenses
		4. Exit 
		""")

def add_expenses():
    while True:
        try:
            date_string = input("Enter date in this format yyyy-mm-dd: ")
            date_object = datetime.strptime(date_string, "%Y-%m-%d")  
            break  
        except ValueError:
            print("Invalid date format. Please enter the correct format (yyyy-mm-dd).")

    while True:
        description = input("Enter the description (or -1 to stop): ")  

        if description == "-1":  
            break  

        while True:
            try:
                amount = float(input("Enter amount: "))
                break  
            except ValueError:
                print("Invalid input. Enter a valid amount.")
        
        
        expense_tracker.append({"Date": date_object, "Description": description, "Amount": amount})
        print("Expense added successfully!")

        break  
        
        print()

			
def view_all_expenses():
    if not expense_tracker:
        print("No expenses yet")
        return  

    print("Expenses:")
    for expense in expense_tracker:
        print(f"Date: {expense['Date'].date()} \tDescription: {expense['Description']} \tAmount: {expense['Amount']:.2f}")
        
    print()

	
def calculate_total_expenses():
    if not expense_tracker:
        print("you never buy anything nah WHY!!")
        return
			
    total_amount = sum(expense["Amount"] for expense in expense_tracker)
    print(f"Total_amount: {total_amount:.2f}")
			
    print()		    
	
	
def exit():
		print("Existing the app. Goodbye!")


def main():
    while True:
        menu()
        try:
            user_input = int(input("Enter a number (1-4): "))
        except ValueError:
        
            print("Please enter a valid number.")
            continue

        if user_input == 1:
            add_on_expenses()
        elif user_input == 2:
            view_all_expenses()
        elif user_input == 3:
            calculate_total_expenses()
        elif user_input == 4:
            exit()
        else:
            print("Invalid input. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
	
		

	
		

