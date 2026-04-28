from data import balance, transactions

def check_balance():
    return balance

def deposit(amount):
    global balance
    balance += amount
    transactions.append(f"Deposited: {amount}")

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        transactions.append(f"Withdrawn: {amount}")
    else:
        return "Insufficient balance"

def get_statement():
    return transactions