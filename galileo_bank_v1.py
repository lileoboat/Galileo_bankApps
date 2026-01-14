# Galileo Central Bank

print("=" * 40)
print("Welcome to Galileo Central Bank")
print("-" * 40)

# Variables for the bank
bank_name = "Galileo Central Bank"
customer_name = ""
account_balance = 0.0
account_number = ""

# User input for customer details
print("Please enter your details to create an account.")
customer_name = input("Please enter your name: ")
account_number = input("Please choose a 4-digit number: ")

# Users initial deposit
initial_deposit = input("Enter initial deposit: $")

# Convert string to number
try:
    account_balance = float(initial_deposit)
    print(f"Thank you, {customer_name}. Your account has been created with an initial balance of ${account_balance:.2f}.")
except:
    print("Please enter a valid number" )

while True:
    print("\n" + "=" * 50)
    print("MAIN MENU")
    print("=" * 30)
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Chhose an option (1-4): ")

    if choice == "1":
        print(f"Current balance: ${account_balance:.2f}")

    elif choice == "2":
        amount = input("How much do you want to deposit? $")
        try:
            amount_num = float(amount)
            account_balance += amount_num
            print(f"${amount_num:.2f} deposited successfully.")
            print(f"New balance: ${account_balance:.2f}")
        except:
            print("please enter a valid number.")
    elif choice == "3":
        amount = input("How much do you want to withdraw? $")
        try:
            amount_num = float(amount)
            if amount_num > account_balance:
                print("Insufficient funds.")
            else:
                account_balance -= amount_num
                print(f"${amount_num:.2f} withdrawn successfully.")
                print(f"New balance: ${account_balance:.2f}")
        except:
            print("please enter a valid number.")
    elif choice == "4":
        print("Thank you for banking with Galileo Central Bank.")
        print(f"Final balance: ${account_balance:.2f}")
        break
    else:
        print("Invalid option. Please choose a number between 1 and 4.")

print("Bank closed"),
        