
from datetime import date
def add_expense(expenses):
        
        description = input("Enter Description: ").strip()
        if description == "" or not any(char.isalpha() for char in description):
            print("Description must contain letters.")
            return
        try:
            amount = float(input("Enter Amount: "))
        except ValueError:
            print("Enter amount in numbers")
            return
        category = input("Enter Category: ").strip()

        if not category or not any(c.isalpha() for c in category):
            print("Invalid category! Enter letters.")
            return

        expense = {
            "description": description,
            "amount": amount,
            "category": category,
            "date": str(date.today())
        }

        expenses.append(expense)
        print("Expense added successfully!")
def view_expenses(expenses):
    for item in expenses:
        print("Description:", item["description"])
        print("Amount:", item["amount"])
        print("Category:", item["category"])
        print("Date:",item["date"])
        print("----------------")
def total_expense(expenses):
    total=0
    for item in expenses:
        total+=item["amount"]
    print("Total:",total)
def delete_expense(expenses):
    view_expenses(expenses)
    try:
        index = int(input("Enter expense number to delete: ")) - 1
        if 0 <= index < len(expenses):
            expenses.pop(index)
            print("Expense deleted successfully!")
        else:
            print("Invalid expense number.")
    except ValueError:
        print("Please enter a valid number.")  
    save_expenses(expenses)
import json
def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)
    print("Expenses saved successfully")
def load_expenses():
    try:
        with open("expenses.json","r") as file:
            expenses=json.load(file)
            return expenses
    except FileNotFoundError:
        print("File not found Starting with empty expenses.")
        return []
expenses=load_expenses()
def search_expenses(expenses):
   search= input("enter category to search:")
   found=False
   for item in expenses:
       if search.lower() == item["category"].lower():
            print("Description:", item["description"])
            print("Amount:", item["amount"])
            print("Category:", item["category"])
            print("Date:", item["date"])
            print("----------------")
            found=True
   if not found:
       print("No expenses found in this category.")
def monthly_expenses(expenses):
    month=input("enter year and month (YYYY-MM):")
    total=0
    for item in expenses:
        if item["date"][:7] == month:
            total += item["amount"]
    print("Total expenses for", month, ":", total)

while True:
    print("===== EXPENSE TRACKER =====")
    print("1.Add expense")
    print("2.View expense")
    print("3.Calculate total")
    print("4.Delete expense")
    print("5.Save expenses")
    print("6.Search expenses")
    print("7.Monthly expenses list")
    print("8.Exit")
    try:
        choice=int(input("enter your choice from 1 to 8:"))
    except ValueError:
        print("enter a number from 1 to 8 only")
        continue
    if choice==1:
        add_expense(expenses)
    elif choice==2:
        view_expenses(expenses)
    elif choice==3:
        total_expense(expenses)
    elif choice==4:
        delete_expense(expenses)
    elif choice==5:
        save_expenses(expenses)
    elif choice==6:
        search_expenses(expenses)
    elif choice==7:
        monthly_expenses(expenses)
    elif choice==8:
        save_expenses(expenses)
        print("Thank you for using Expense Tracker!")
        break
    else:
        print("Please choose a number from 1 to 8")
