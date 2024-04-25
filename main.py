#To manage bank accounts:

#Create a bank account with a number and PIN.
#Deposit money into the account.
#Withdraw money from the account.
#Change the account's PIN.

#To use the system:

#Start.
#Choose: create an account, log in, or exit.
#If creating an account:
#Enter a number and a PIN.
#Account created!
#If logging in:
#Enter your account number and PIN.
#If correct:
#Deposit, withdraw, or change PIN.
#Log out to finish.
#If incorrect:
#Try again or exit.
#If exiting:
#End.

#limit it to only 4 characters for the pin and only numbers

import mysql.connector

# Function to establish connection to MySQL database
def connect_to_database():
    try:
        connection = mysql.connector.connect(user='root', database='bank', password='Tunc2009')
        return connection
    except mysql.connector.Error as err:
        print("Error connecting to MySQL database:", err)
        return None

# Function to create a new account in the database
def create_account(account_number, pin):
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            insert_query = "INSERT INTO accounts (account_number, pin, balance) VALUES (%s, %s, 0)"
            cursor.execute(insert_query, (account_number, pin))
            connection.commit()
            print("Account created successfully.")
            cursor.close()
    except mysql.connector.Error as err:
        print("Error creating account:", err)
    finally:
        if connection:
            connection.close()

# Function to retrieve account information from the database
def get_account(account_number):
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor(dictionary=True)
            select_query = "SELECT * FROM accounts WHERE account_number = %s"
            cursor.execute(select_query, (account_number,))
            return cursor.fetchone()
    except mysql.connector.Error as err:
        print("Error retrieving account:", err)
        return None
    finally:
        if connection:
            connection.close()

# Function to update account balance in the database
def update_balance(account_number, new_balance):
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            update_query = "UPDATE accounts SET balance = %s WHERE account_number = %s"
            cursor.execute(update_query, (new_balance, account_number))
            connection.commit()
            cursor.close()
    except mysql.connector.Error as err:
        print("Error updating balance:", err)
    finally:
        if connection:
            connection.close()

# Function to update account PIN in the database
def update_pin(account_number, new_pin):
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            update_query = "UPDATE accounts SET pin = %s WHERE account_number = %s"
            cursor.execute(update_query, (new_pin, account_number))
            connection.commit()
            cursor.close()
    except mysql.connector.Error as err:
        print("Error updating PIN:", err)
    finally:
        if connection:
            connection.close()

def deposit(account_number, amount):
    account = get_account(account_number)
    if account:
        new_balance = account['balance'] + amount
        update_balance(account_number, new_balance)
        print(f"Deposit successful. New balance: {new_balance}")
    else:
        print("Account not found.")

def withdraw(account_number, amount):
    account = get_account(account_number)
    if account:
        if amount <= account['balance']:
            new_balance = account['balance'] - amount
            update_balance(account_number, new_balance)
            print(f"Withdrawal successful. New balance: {new_balance}")
        else:
            print("Insufficient funds.")
    else:
        print("Account not found.")

def change_pin(account_number, new_pin):
    account = get_account(account_number)
    if account:
        update_pin(account_number, new_pin)
        print("PIN changed successfully.")
    else:
        print("Account not found.")

def main():
    print("Welcome to Our Bank!")

    while True:
        print("\n1. Create Account\n2. Login\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            account_number = input("Enter account number: ")
            pin = input("Set pin: ")
            create_account(account_number, pin)

        elif choice == "2":
            account_number = input("Enter account number: ")
            account = get_account(account_number)
            if account:
                pin = input("Enter pin: ")
                if pin == account['pin']:
                    while True:
                        print("\n1. Deposit\n2. Withdraw\n3. Change PIN\n4. Logout")
                        user_choice = input("Enter your choice: ")

                        if user_choice == "1":
                            amount = float(input("Enter amount to deposit: "))
                            deposit(account_number, amount)

                        elif user_choice == "2":
                            amount = float(input("Enter amount to withdraw: "))
                            withdraw(account_number, amount)

                        elif user_choice == "3":
                            new_pin = input("Enter new pin: ")
                            update_pin(account_number, new_pin)

                        elif user_choice == "4":
                            print("Logged out.")
                            break

                else:
                    print("Incorrect pin.")

            else:
                print("Account not found.")

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
