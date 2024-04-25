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

# Establishing connection to MySQL database
connection = mysql.connector.connect(user='root', database='bank', password='Tunc2009')
cursor = connection.cursor()

# Displaying existing accounts (just for testing)
testQuery = "SELECT * FROM accounts"
cursor.execute(testQuery)
for item in cursor:
    print(item)
cursor.close()

# Function to deposit money into the account
def deposit(account_number, amount):
    cursor = connection.cursor()
    update_query = f"UPDATE accounts SET balance = balance + {amount} WHERE account_number = '{account_number}'"
    cursor.execute(update_query)
    connection.commit()
    print("Deposit successful.")
    cursor.close()

# Function to withdraw money from the account
def withdraw(account_number, amount):
    cursor = connection.cursor()
    update_query = f"UPDATE accounts SET balance = balance - {amount} WHERE account_number = '{account_number}' AND balance >= {amount}"
    cursor.execute(update_query)
    connection.commit()
    if cursor.rowcount > 0:
        print("Withdrawal successful.")
    else:
        print("Insufficient funds.")
    cursor.close()

# Function to change the account's PIN
def change_pin(account_number, new_pin):
    cursor = connection.cursor()
    update_query = f"UPDATE accounts SET pin = '{new_pin}' WHERE account_number = '{account_number}'"
    cursor.execute(update_query)
    connection.commit()
    print("PIN changed successfully.")
    cursor.close()

def main():
    print("Welcome to Our Bank!")

    while True:
        print("\n1. Create Account\n2. Login\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            account_number = input("Enter account number: ")
            pin = input("Set PIN (4 characters, only numbers): ")
            cursor = connection.cursor()
            insert_query = f"INSERT INTO accounts (account_number, pin, balance) VALUES ('{account_number}', '{pin}', 0)"
            cursor.execute(insert_query)
            connection.commit()
            print("Account created successfully.")
            cursor.close()

        elif choice == "2":
            account_number = input("Enter account number: ")
            pin = input("Enter PIN: ")
            cursor = connection.cursor(dictionary=True)
            select_query = f"SELECT * FROM accounts WHERE account_number = '{account_number}' AND pin = '{pin}'"
            cursor.execute(select_query)
            account = list(cursor)
            if account:
                print("Login successful.")
                while True:
                    print("\n1. Deposit\n2. Withdraw\n3. Change PIN\n4. Logout")
                    user_choice = input("Enter your choice: ")

                    if user_choice == "1":
                        amount = int(input("Enter amount to deposit: "))
                        deposit(account_number, amount)

                    elif user_choice == "2":
                        amount = int(input("Enter amount to withdraw: "))
                        withdraw(account_number, amount)

                    elif user_choice == "3":
                        new_pin = input("Enter new PIN (4 characters, only numbers): ")
                        change_pin(account_number, new_pin)

                    elif user_choice == "4":
                        print("Logged out.")
                        break

            else:
                print("Incorrect account number or PIN.")
            cursor.close()

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

# Resetting the table
cursor = connection.cursor()
reset_query = "DELETE FROM accounts"
cursor.execute(reset_query)
connection.commit()
cursor.close()

if __name__ == "__main__":
    main()

# Closing the connection to MySQL database
connection.close()
