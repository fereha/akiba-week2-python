# ===== AKIBA BANK - Simple Bank Account System =====
# --- Starting values ---
correct_pin = "1234"
max_attempts = 3
attempts = 0
pin_correct = False

balance = 1000        # starting balance in Birr
transactions = 0      # counts successful deposits and withdrawals (bonus)

# --- PIN system (challenge) ---
print("===== AKIBA BANK =====")

while attempts < max_attempts and pin_correct == False:
    pin = input("Enter your PIN: ")
    attempts = attempts + 1

    if pin == correct_pin:
        pin_correct = True
        print("PIN correct!")
        print("Welcome to Akiba Bank.")
    else:
        print("Incorrect PIN.")
        if attempts < max_attempts:
            print("Attempts remaining:", max_attempts - attempts)

# --- If the PIN was never entered correctly, lock the account ---
if pin_correct == False:
    print("Too many incorrect attempts.")
    print("Your account is locked.")

# --- Otherwise, show the bank menu ---
else:
    running = True

    while running:
        print()
        print("===== AKIBA BANK =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        choice = input("Choose an option: ")

        # Feature 1: Check balance
        if choice == "1":
            print("Your current balance is:", balance, "Birr")

        # Feature 2: Deposit
        elif choice == "2":
            amount_text = input("Enter deposit amount: ")

            if amount_text.isdigit():
                amount = int(amount_text)

                if amount > 0:
                    balance = balance + amount
                    transactions = transactions + 1
                    print("Deposit successful!")
                    print("Your new balance is:", balance, "Birr")
                else:
                    print("Amount must be greater than zero.")
            else:
                print("Invalid amount. Please enter a positive whole number.")

        # Feature 3: Withdraw
        elif choice == "3":
            amount_text = input("Enter withdrawal amount: ")

            if amount_text.isdigit():
                amount = int(amount_text)

                if amount <= 0:
                    print("Amount must be greater than zero.")
                elif amount > balance:
                    print("Insufficient balance!")
                else:
                    balance = balance - amount
                    transactions = transactions + 1
                    print("Withdrawal successful!")
                    print("Your new balance is:", balance, "Birr")
            else:
                print("Invalid amount. Please enter a positive whole number.")

        # Feature 4: Exit
        elif choice == "4":
            print("Transactions made:", transactions)
            print("Thank you for using Akiba Bank!")
            print("Goodbye!")
            running = False

        # Feature 5: Invalid option
        else:
            print("Invalid option.")
            print("Please choose a valid option.")