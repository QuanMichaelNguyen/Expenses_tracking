from expenses import Expense
import calendar
import datetime
from utils import get_user_expense, save_expense_to_file, summarize_expense
def main():
    print(f" This is your Expense Tracker!")
    expense_file_path = "expenses.csv"
    budget = float(input("Your budget is: "))
    # Get user input for expense
    expense = get_user_expense()
    # Write their expense to a file
    save_expense_to_file(expense, expense_file_path)
    # Read file and summarize expense
    summarize_expense(expense_file_path, budget)
    
# only run when we run this file
if __name__ == "__main__":
    main()