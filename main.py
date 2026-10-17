# lab4.py
# Partners: Adolfo & David
# Main driver program

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




import module_adolfo
import module_david

def main():  # Written by David and Adolfo
    balance = 0.0
    print("Welcome to the Partner Banking App!")

    while True:
        print_menu()
        choice = get_choice()

        if choice == 1:
            module_adolfo.view_balance(balance)

        elif choice == 2:
            amount = module_adolfo.get_amount("Enter deposit amount: ")
            balance = module_adolfo.deposit(balance, amount)
            print(f"Deposit successful! New balance: ${balance:.2f}")

        elif choice == 3:
            amount = module_david.get_amount("Enter withdrawal amount: ")
            balance = module_david.withdrawal(balance, amount)

        elif choice == 4:
            module_david.show_transactions()

        elif choice == 5:
            print("\nThank you for using the Partner Banking App!")
            break



def print_menu():    #Written by David
    print("\n=== Banking Menu ===")
    print("1. View Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Show Transactions")
    print("5. Quit")

def get_choice():    # Written by David and Adolfo
    QUIT = 5
    while True:
        try:
            choice = int(input("Enter your choice (1-5): "))
            if 1 <= choice <= QUIT:
                return choice
            else:
                print("Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == '__main__':
    main()