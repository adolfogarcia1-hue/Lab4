# Module written by Adolfo

def view_balance(balance):
    print(f"Current balance:: ${balance:.2f}")

def deposit(balance, amount):
    return balance + amount

def view_amount(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Amount must be greater than 0")
            else:
                return value
        except ValueError:
            print("Invalid input. Enter a number please.")

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
