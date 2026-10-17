# *********************************************************
# Authors:      David Schaper
# File:         module_david.py
# Date:         10/17/2026


def withdrawal(balance, amount):
    while amount > balance:
        print("Insufficient funds.")
        amount = get_amount("Enter withdrawal amount: ")

    return balance - amount , amount


def show_transactions(transaction_list, transaction_amounts, balance):
    if len(transaction_list) == 0:
        print("No transactions yet.")
    else:
        print("\n====== Transaction History ======")
        names = transaction_list.split(",")
        amounts = transaction_amounts.split(",")

        for i in range(len(names)):
            if names[i] != "" and amounts[i] != "":
                print(f"{names[i]:<23} ${amounts[i]:>10}")
    print(f"{'New balance:':<23} ${balance:>10.2f}")


# Written by Adolfo
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
