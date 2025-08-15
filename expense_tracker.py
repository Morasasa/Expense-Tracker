expenses = []  

def add_expense():
    amount = float(input("Enter amount: ₹"))
    category = input("Enter category (Food, Travel, Shopping, etc.): ")
    expenses.append({"amount": amount, "category": category})
    print("Expense added successfully!")

def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\n---- Your Expenses ----")
    total = 0
    for i, expense in enumerate(expenses, 1):
        print(f"{i}. ₹{expense['amount']} - {expense['category']}")
        total += expense["amount"]
    print(f"Total Expenses: ₹{total}")

def main():
    while True:
        print("\n===== Expense Tracker Menu =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("💰 Thank you for using Expense Tracker!")
            break
        else:
            print(" Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
