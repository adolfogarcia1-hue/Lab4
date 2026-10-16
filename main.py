# lab4.py
# Partners: Adolfo & David
# Main driver program

import module_adolfo
import module_david

QUIT = 4

def print_menu():
    print("\n=== Banking Menu ===")
    print("1. View Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Quit")

def get_choice():
    while True:
        try:
            choice = int(input("Enter your choice (1-4): "))
            if 1 <= choice <= QUIT:
                return choice
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    balance = 0.0
    print("Welcome to the Partner Banking App!")

main()