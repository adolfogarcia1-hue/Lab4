# lab4.py
# Partners: Adolfo & David
# Main driver program

import module_adolfo
import module_david

def main():
    balance = 0.0
    print("Welcome to the Partner Banking App!")
    print_menu()
    choice = get_choice()
    match choice:
        case 1:
            module_adolfo.view_balance()
        case 2:
            module_adolfo.deposit()
        case 3:
            module_david.withdrawal()
        case 4:
            module_david.show_transactions()
        case _:
            pass


def print_menu():
    print("\n=== Banking Menu ===")
    print("1. View Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Show Transactions")
    print("5. Quit")

def get_choice():
    QUIT = 5
    while True:
        try:
            choice = int(input("Enter your choice (1-5): "))
            if 1 <= choice <= QUIT:
                return choice
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == '__main__':
    main()