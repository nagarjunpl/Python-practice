'''Create a Python program using OOP to manage savings and current bank accounts.
Include features like deposit, withdraw, balance check, and interest calculation.'''


# ---- Base Account Class ----
class Account:
    def __init__(self, account_id, holder_name):
        # Constructor to initialize account with ID and holder name
        self.account_id = account_id
        self.holder_name = holder_name
        self._balance = 0  # Protected attribute to store balance

    def check_balance(self):
        # Method to print the current balance
        print(f"Balance: ₹{self._balance:.2f}")

    def deposit(self, amount):
        # Method to deposit money into the account
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
        self._balance += amount
        print(f"Deposit successful. Updated Balance: ₹{self._balance:.2f}")

    def withdraw(self, amount):
        # Method to withdraw money if sufficient balance exists
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
        if self._balance >= amount:
            self._balance -= amount
            print(f"Withdraw successful. Updated Balance: ₹{self._balance:.2f}")
        else:
            print("Insufficient balance.")

    def __str__(self):
        # String representation of account details
        return f"Account ID: {self.account_id}, Holder: {self.holder_name}, Balance: ₹{self._balance:.2f}"


# ---- Savings Account Class ----
class SavingsAccount(Account):
    def calculate_interest(self):
        # Method to calculate and print interest at 4% rate
        interest_rate = 0.04  # 4% interest
        interest = self._balance * interest_rate
        print(f"Interest on balance: ₹{interest:.2f}")


# ---- Current Account Class ----
class CurrentAccount(Account):
    def withdraw(self, amount):
        # Overridden withdraw method with overdraft facility
        over_draft_limit = 1000  # Allow ₹1000 overdraft
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
        if self._balance + over_draft_limit >= amount:
            self._balance -= amount
            print(f"Withdraw successful. Updated Balance: ₹{self._balance:.2f}")
        else:
            print("Withdrawal amount exceeds overdraft limit.")


# ---- Bank Class ----
class Bank:
    def __init__(self, name, city):
        # Constructor to initialize bank with name and city
        self.__name = name
        self.__city = city
        self.__accounts = {}  # Dictionary to hold account objects

    def create_account(self, account_id, holder_name, acc_type):
        # Method to create either a savings or current account
        if account_id in self.__accounts:
            print("Account ID already exists.")
            return None

        if acc_type == "savings":
            new_account = SavingsAccount(account_id, holder_name)
        elif acc_type == "current":
            new_account = CurrentAccount(account_id, holder_name)
        else:
            print("Invalid account type.")
            return None

        self.__accounts[account_id] = new_account
        print("Account creation successful.")
        return new_account

    def get_account(self, account_id):
        # Fetch and return account object by ID
        if account_id not in self.__accounts:
            print("Account not found.")
            return None
        acc = self.__accounts[account_id]
        print(f"\nAccount Details:\n{acc}")
        return acc


# ---- Main Menu Driven Program ----
npl = Bank("SBI", "Mandya")  # Creating Bank object

# Infinite loop for menu interaction
while True:
    # Display main menu options
    print("\n--- Welcome to Nagarjun Bank ---")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Calculate Interest (Savings Only)")
    print("6. Exit")
    
    choice = input("Enter your choice: ")  # User input

    if choice == '1':
        # Create a new account
        acc_id = input("Enter Account ID: ")
        name = input("Enter Holder Name: ")
        acc_type = input("Enter Account Type (savings/current): ").lower()
        npl.create_account(acc_id, name, acc_type)

    elif choice == '2':
        # Deposit into an existing account
        acc_id = input("Enter Account ID: ")
        acc = npl.get_account(acc_id)
        if acc:
            amt = input("Enter amount to deposit: ")
            if amt.replace('.', '', 1).isdigit():
                acc.deposit(float(amt))
            else:
                print("Invalid input. Enter a valid number.")

    elif choice == '3':
        # Withdraw from an account
        acc_id = input("Enter Account ID: ")
        acc = npl.get_account(acc_id)
        if acc:
            amt = input("Enter amount to withdraw: ")
            if amt.replace('.', '', 1).isdigit():
                acc.withdraw(float(amt))
            else:
                print("Invalid input. Enter a valid number.")

    elif choice == '4':
        # Check balance for an account
        acc_id = input("Enter Account ID: ")
        acc = npl.get_account(acc_id)
        if acc:
            acc.check_balance()

    elif choice == '5':
        # Calculate interest for savings account
        acc_id = input("Enter Account ID: ")
        acc = npl.get_account(acc_id)
        if isinstance(acc, SavingsAccount):
            acc.calculate_interest()
        else:
            print("Interest calculation only for savings accounts.")

    elif choice == '6':
        # Exit the application
        print("Thank you for banking with Nagarjun Bank. Goodbye!")
        break

    else:
        # Handle invalid menu choices
        print("Invalid choice. Please try again.")
