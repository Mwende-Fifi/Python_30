#This is a personal expenses tracker


"""
Developing a personal expense tracker that allows 
users to add, 
view expenses.
exit the function

"""
# dependencies
import os
import csv
from datetime import datetime

print("Welcome to the personal expenses tracker")

# add expenses

def add_expenses(description, amount):

    # creating a csv file to store the expenses data
    with open("personal_expense.csv", "a", newline = "") as file:
        line = csv.writer(file)
        line.writerow([description, amount, datetime.now().strftime("%d/%m/%Y, %H:%M:%S")])

    print("Expenses Recorded")

# view expenses
def view_expenses():
        if os.path.exists("personal_expense.csv"):
            with open("personal_expense.csv", "r") as file:
                expenses = csv.reader(file)
                for expense in expenses:
                    print(f"\nExpense_Name : {expense[0]}, Amount : {expense[1]}$, Date : {expense[2]}")
        else:
            print("No expenses found!")

def main():
    while True:
        print('1. Add expenses')
        print('2. View expenses')
        print('3. exit')
        choose = input("Please select any option from the above: ")

        if choose == '1':
            description = input("Please enter description: ")
            amount = float(input("Please enter amount: "))

            # adding the expenses
            add_expenses(description, amount)

        elif choose == '2':
            view_expenses()


        elif choose == '3':
            print("Thank you for closing the app.")
            break


        else:
            print("Invalid choice! Please try again!")

if __name__ == '__main__':
    main()