"""expense_tracker/transactions.py"""
class Transaction:
    def __init__(self, t_type, amount, category, date):
        if t_type not in ["доход", "расход"]:
            raise ValueError("Тип транзакции должен быть либо 'доход', либо 'расход'")
        if amount <= 0:
            raise ValueError("Сумма должна быть положительным числом")

        self.t_type = t_type
        self.amount = amount
        self.category = category
        self.date = date

    def __str__(self):
        return f"[{self.date}] {self.t_type.capitalize()}: {self.amount} ({self.category})"