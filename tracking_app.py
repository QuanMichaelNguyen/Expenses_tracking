from flask import Flask, render_template
import csv

app = Flask(__name__)

@app.route('/')
def index():
    # Read expenses from the CSV file
    expenses = read_expenses_from_csv("expenses.csv")
    return render_template('index.html', expenses=expenses)

def read_expenses_from_csv(file_path):
    expenses = []
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if len(row) == 3:
                name, amount, category = row
                expenses.append({'name': name, 'amount': float(amount), 'category': category})
    return expenses

if __name__ == '__main__':
    app.run(debug=True)
