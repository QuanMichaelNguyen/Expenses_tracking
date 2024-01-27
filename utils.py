import calendar
import datetime
from expenses import Expense
import csv
import matplotlib.pyplot as plt
def get_user_expense():
    print("Getting User Expense")
    expense_name = input("Enter expense name: ")
    # Store multiple expenses
    expenses_list = []
    while expense_name.lower() != "done":
        expense_amount = float(input("Enter expense amount: "))

        expense_categories = ["Food", "Rent", "Electricity", "Utilities", "Fun", "Misc"]

        while True:
            print("Select a category: ")
            for i, category_name in enumerate(expense_categories):
                print(f"{i+1}. {category_name}")
            range_to_choose = f"[1- {len(expense_categories)}]"
            try:
                # -1 to return to actual index of expenses_categories
                selected_index = int(input(f"Enter a category number {range_to_choose}: ")) - 1
            except ValueError:
                pass
            if selected_index in range(len(expense_categories)):
                selected_category = expense_categories[selected_index]
                # make an instance of Expense class
                new_expense = Expense(name = expense_name, category=selected_category, amount=expense_amount)
                # return new_expense
                expenses_list.append(new_expense)
                break
            else:
                print("Please choose valid category again")
        expense_name = input("Enter expense name (or type 'done' to finish): ")

    return expenses_list

def save_expense_to_file(expenses, expense_file_path):
    # print(f"Saving User Expense: {expense} to {expense_file_path}")
    print(f"Saving User Expenses to {expense_file_path}")

    with open(expense_file_path, "a") as f:
        for expense in expenses:
            f.write(f"{expense.name},{expense.amount},{expense.category}\n")


def summarize_expense(expense_file_path, budget):
    print("Summarizing User Expense")
    expenses: list[Expense] = []
    with open(expense_file_path, "r") as f:
        #
        csv_reader = csv.reader(f)
        for row in csv_reader:
            if len(row) == 3:
                expense_name, expense_amount, expense_category = row
                line_expense = Expense(
                    name=expense_name,
                    amount=float(expense_amount),
                    category=expense_category
                )
                expenses.append(line_expense)

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount
    print("Expenses By Category 📈")
    for key, amount in amount_by_category.items():
        print(f" {key}: ${amount:.2f}")

    total_spent = sum([x.amount for x in expenses])

    print(f"Total spent: ${total_spent:.2f}")

    remaining_budget = budget - total_spent
    if remaining_budget > 0:
        print(f"Budget remaining: ${remaining_budget:.2f}")
        # Get the current date
        now = datetime.datetime.now()

        # Get the number of days in the current month
        days_in_month = calendar.monthrange(now.year, now.month)[1]

        # Calculate the remaining number of days in the current month
        remaining_days = days_in_month - now.day

        print("Remaining days in the current month:", remaining_days)

        if remaining_days > 0:
            daily_budget = remaining_budget / remaining_days
            print(f"Budget per day: ${daily_budget:.2f}")
        else:
            print("Remaining days in the current month is zero")
            daily_budget = 0
    else:
        print(f"Out of budget: {remaining_budget} ")
    
    
    categories = list(amount_by_category.keys())
    amounts = list(amount_by_category.values())

    plt.bar(categories, amounts, color = 'green')
    plt.xlabel('Expense Categories')
    plt.title('Expense Distribution')
    plt.xticks(rotation = 45, ha = 'right')
    plt.show()
