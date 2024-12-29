"""expense_tracker/tracker.py"""
import datetime
from expense_tracker.transactions import Transaction

class ExpenseTracker:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, t_type, amount, category, date=None):
        if not date:
            date = datetime.datetime.now().strftime("%Y-%m-%d")
        transaction = Transaction(t_type, amount, category, date)
        self.transactions.append(transaction)

    def view_transactions(self):
        for t in self.transactions:
            print(t)

    def generate_report(self):
        income = sum(t.amount for t in self.transactions if t.t_type == "доход")
        expense = sum(t.amount for t in self.transactions if t.t_type == "расход")
        print(f"Общий доход: {income}")
        print(f"Общие расходы: {expense}")
        print(f"Баланс: {income - expense}")