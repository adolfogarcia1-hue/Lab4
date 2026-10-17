# *********************************************************
# Authors:      David Schaper and Adolfo Garcia
# Project Name: lab4.py
# File:         main.py
# Date:         10/17/2026
# Description:  Banking program takes deposits and withdrawals
#               and displays balances and transactions
# Source:       CIS 133Y Assignment – Banking App
# Inputs:       Menu options, dollar amounts
#
# Output:       Balances, transaction

# Sample Run:
# Welcome to the Partner Banking App!
# 1. View Balance
# 2. Deposit
# 3. Withdraw
# 4. Show Transactions
# 5. Quit
# Enter your choice: 2
# Enter deposit amount: 50
# Deposit successful! New balance: $50.00
# *********************************************************

import module_adolfo
import module_david


def main():  # Written by David and Adolfo
    balance = 0.0
    transaction_list = ""
    transaction_amounts =""

    print("Welcome to the Partner Banking App!")

    while True:
        print_menu()
        choice = get_choice()

        # Displays Balance, Written by Adolfo
        if choice == 1:
            module_adolfo.view_balance(balance)

        # Adds a deposit, Written by Adolfo, transaction lists by David
        elif choice == 2:
            amount = module_adolfo.get_amount("Enter deposit amount: ")
            amount = float(f"{amount:.2f}")
            balance = module_adolfo.deposit(balance, amount)
            transaction_list += "Deposit,"
            transaction_amounts += f"{float(amount):.2f},"
            print(f"Deposit successful! New balance: ${balance:.2f}")

        # Makes a withdrawal, Written by David
        elif choice == 3:
            amount = module_david.get_amount("Enter withdrawal amount: ")
            amount = float(f"{amount:.2f}")
            balance , amount = module_david.withdrawal(balance, amount)
            transaction_list += "Withdrawal,"
            transaction_amounts += f"{float(amount):.2f},"
            print(f"Withdrawal successful! New balance: ${balance:.2f}")

        # Shows a list of transactions, Written by David
        elif choice == 4:
            module_david.show_transactions(transaction_list,
                                           transaction_amounts, balance)

        # Exits program, Written by Adolfo
        elif choice == 5:
            print("\nThank you for using the Partner Banking App!")
            break


def print_menu():    # Written by David
    print("\n=== Banking Menu ===")
    print("1. View Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Show Transactions")
    print("5. Quit")

def get_choice():    # Written by David and Adolfo
    quit_choice = 5
    while True:
        try:
            choice = int(input("Enter your choice (1-5): "))
            if 1 <= choice <= quit_choice:
                return choice
            else:
                print("Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == '__main__':
    main()