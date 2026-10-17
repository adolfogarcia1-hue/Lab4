# Module written by David

# This list stores transactions
transactions = []

def withdrawal(balance, amount):
    if amount <= 0:
        print("Withdrawal amount must be greater than 0.")
        return balance

    if amount > balance:
        print("Insufficient funds.")
        return balance

    new_balance = balance - amount
    transactions.append(f"Withdrew ${amount:.2f}")
    return new_balance


def show_transactions():
    if len(transactions) == 0:
        print("No transactions yet.")
    else:
        print("\n=== Transaction History ===")
        for t in transactions:
            print(t)

def get_amount(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Amount must be greater than 0.")
            else:
                return value
        except ValueError:
            print("Invalid input. Enter a number.")
