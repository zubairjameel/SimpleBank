import random

def bank_system():
    print("Welcome to the National Bank")
    user_input = input("Enter your name: ")
    print("How can I help you?")

    options = [
        "1. Account Opening\n",
        "2. Cash deposit\n",
        "3. Cash withdrawal\n",
        "4. Account balance\n",
        "5. Exit\n"
    ]

    for option in options:
        print(option, end='')

    account_created = False
    account_balance = 0

    while True:
        user_choice = input("Please choose an option: ")

        if user_choice == "1":
            print("Opening account")
            input_1 = input("Enter your name: ")
            input_2 = input("Enter your age: ")
            input_3 = input("Enter your phone number: ")
            input_4 = input("Enter your address: ")
            print("Thank you for choosing National Bank. Your account is successfully created.")
            print("Your Account Number is", random.randint(1000000000, 9999999999))
            account_created = True 
          
        elif user_choice == "2":
            if not account_created:
                print("You need to create an account first.")
            else:
                cash_deposit = float(input("Enter the amount you want to deposit: "))
                account_balance += cash_deposit
                print(f"Amount deposited: {cash_deposit}. Your new balance is {account_balance}.")

        elif user_choice == "3":
            if not account_created:
                print("You need to create an account first.")
            else:
                cash_withdrawal = float(input("Enter the amount you want to withdraw: "))
                if cash_withdrawal > account_balance:
                    print("Insufficient balance.")
                else:
                    account_balance -= cash_withdrawal
                    print(f"Amount withdrawn: {cash_withdrawal}. Your new balance is {account_balance}.")

        elif user_choice == "4":
            if not account_created:
                print("You need to create an account first.")
            else:
                print(f"Your current balance is {account_balance}.")

        elif user_choice == "5":
            print("Thank you for using National Bank. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

bank_system()
