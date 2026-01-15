import json

print("=" * 40)
print("Welcome to Galileo Central Bank - Version 2")
print("-" * 40)

# A dictionary to store account info
account = {
    "name" : "",
    "balance" : 0.0,
    "account_type" : "savings",
    "transactions" : []
}

# A list for multiple accounts
all_accounts = []

# Set for unique account types
account_types = {"savings", "checking", "business"}

#Tuples for fixed data
bank_info = ("Galileo Central Bank", "Est.2018", "24/7")

# Get user info
print(f"\nBank info: {bank_info[0]}, {bank_info[1]}, Services: {bank_info[2]}")
account["name"] = input("Enter your name to create an account: ")

print(f"\nAccount types available:")
for acc_type in account_types:
    print(f"  - {acc_type}")

account["account_type"] = input("Choose an account type from above: ").lower()

# Initial deposits
deposit = float(input("Initial deposit: $"))
account["balance"] = deposit

# Add to all accounts lists
all_accounts.append(account)
print(f"\nAccount created #{len(all_accounts)}")

# Transaction functions
def show_balance():
    print(f"\nBALANCE: ${account['balance']:.2f}")

def deposit_money():
    amount = float(input("Deposit amount: $"))
    account["balance"] += amount
    account["transactions"].append(f"Deposit: +${amount:.2f}")
    print(f"Deposited ${amount:.2f} successfully.")

def withdraw_money():
    amount = float(input("Withdraw amount: $"))
    if amount > account["balance"]:
        print("Insufficient funds.")
    else:
        account["balance"] -= amount
        account["transactions"].append(f"Withdraw: -${amount:.2f}")
        print(f"Withdrew ${amount:.2f} successfully.")

def show_transactions():
    print("\nTRANSACTION HISTORY:")
    if not account["transactions"]:
        print("No transactions yet.")
    else:
        for i, transaction in enumerate(account["transactions"], 1):
            print(f"{i}. {transaction}")

def save_to_file():
    """Save account data to JSON file."""
    try:
        with open("bank_data.json", "w") as file:
            json.dump(account, file, indent=2)
        print("Data saved to bank_data.json")
    except:
        print("Could not save data")

# Main menu
while True:
    print("\n" + "=" * 30)
    print("MAIN MENU")
    print("=" * 30)
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Show Transactions")
    print("5. Save Data")
    print("6. Exit")

    choice = input("\nChoose an option (1-6): ")

    if choice == "1":
        show_balance()
    elif choice == "2":
        deposit_money()
    elif choice == "3":
        withdraw_money()
    elif choice == "4":
        show_transactions()
    elif choice == "5":
        save_to_file()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")