from expenses import Expense
import calendar
import datetime
from utils import get_user_expense, save_expense_to_file, summarize_expense
def main():
    print(f" This is your Expense Tracker!")
    expense_file_path = "expenses.csv"
    budget = float(input("Your budget is: "))
    while True:
        # Get user input for expense
        expense = get_user_expense()
        # Write their expense to a file
        save_expense_to_file(expense, expense_file_path)
        # Read file and summarize expense
        summarize_expense(expense_file_path, budget)
        # Ask the user to add more or not
        another_expense = input("Do you want to add more expenses? (yes/no): ").lower()
        if another_expense != "yes":
            break
    
# only run when we run this file
if __name__ == "__main__":
    main()