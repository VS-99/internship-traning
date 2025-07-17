import json
import os
from datetime import datetime

DATA_FILE = 'expenses.json'

def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_expenses(expenses):
    with open(DATA_FILE, 'w') as f:
        json.dump(expenses, f, indent=2)

def add_expense():
    date = input("Enter date (YYYY-MM-DD) or leave blank for today: ") or datetime.today().strftime('%Y-%m-%d')
    amount = float(input("Enter amount: ₹"))
    category = input("Enter category (e.g., food, travel, bills): ").strip().lower()

    new_expense = {
        "date": date,
        "amount": amount,
        "category": category
    }

    expenses = load_expenses()
    expenses.append(new_expense)
    save_expenses(expenses)
    print("✅ Expense added!")

def view_all():
    expenses = load_expenses()
    if not expenses:
        print("No expenses found.")
        return
    for e in expenses:
        print(f"{e['date']} - ₹{e['amount']} ({e['category']})")

def total_by_category():
    expenses = load_expenses()
    totals = {}
    for e in expenses:
        totals[e['category']] = totals.get(e['category'], 0) + e['amount']
    for cat, total in totals.items():
        print(f"{cat}: ₹{total:.2f}")

def total_by_date():
    expenses = load_expenses()
    totals = {}
    for e in expenses:
        totals[e['date']] = totals.get(e['date'], 0) + e['amount']
    for date, total in totals.items():
        print(f"{date}: ₹{total:.2f}")

def menu():
    while True:
        print("\n📒 Expense Tracker Menu")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Total by Category")
        print("4. Total by Date")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_all()
        elif choice == '3':
            total_by_category()
        elif choice == '4':
            total_by_date()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
