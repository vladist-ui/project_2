"""expense_tracker/exceptions.py"""
class ExpenseTrackerException(Exception):
    pass

class InvalidTransactionTypeException(ExpenseTrackerException):
    def __init__(self, t_type):
        super().__init__(f"Недопустимый тип транзакции: {t_type}")

class NegativeAmountException(ExpenseTrackerException):
    def __init__(self, amount):
        super().__init__(f"Сумма не может быть отрицательной или равной нулю: {amount}")