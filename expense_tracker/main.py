## main.py
"""expense_tracker/main.py"""
from expense_tracker.tracker import ExpenseTracker

# Создаём экземпляр трекера
tracker = ExpenseTracker()

# Добавление примера транзакций
tracker.add_transaction("доход", 10000000, "зарплата", "2024-12-29")
tracker.add_transaction("расход", 500000, "Подарок Никите", "2024-12-29")

# Просмотр транзакций
tracker.view_transactions()

# Генерация отчёта
tracker.generate_report()