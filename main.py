import mysql.connector

# Establishing connection to MySQL database
connection = mysql.connector.connect(user='root', database='bank', password='Tunc2009')
cursor = connection.cursor()

# Function to display all accounts
def display_accounts():
    cursor = connection.cursor()
    select_query = "SELECT account_number, pin, balance FROM accounts"
    cursor.execute(select_query)
    print("\nAll Accounts:")
    for account in cursor:
        print(f"Account Number: {account[0]}, PIN: {account[1]}, Balance: {account[2]}")
    cursor.close()

# Displaying existing accounts (just for testing)
display_accounts()

def deposit(account_number, amount):
    cursor = connection.cursor()
    update_query = f"UPDATE accounts SET balance = balance + {amount} WHERE account_number = '{account_number}'"
    cursor.execute(update_query)
    connection.commit()
    print("Deposit successful.")
    cursor.close()

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

def change_pin(account_number, new_pin):
    cursor = connection.cursor()
    update_query = f"UPDATE accounts SET pin = '{new_pin}' WHERE account_number = '{account_number}'"
    cursor.execute(update_query)
    connection.commit()
    print("PIN changed successfully.")
    cursor.close()

def admin_actions():
    while True:
        print("\nAdmin Options:")
        print("1. View all accounts")
        print("2. Change PIN of an account")
        print("3. Return to main menu")
        admin_choice = input("Enter your choice: ")

        if admin_choice == "1":
            display_accounts()

        elif admin_choice == "2":
            account_number = input("Enter account number to change PIN: ")
            new_pin = input("Enter new PIN (4 characters, only numbers): ")
            change_pin(account_number, new_pin)

        elif admin_choice == "3":
            print("Returning to main menu...")
            break

        else:
            print("Invalid choice. Please try again.")

def main():
    print("Welcome to Our Bank!")

    while True:
        print("\n1. Create Account\n2. Login\n3. Admin Login\n4. Exit")
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
            cursor = connection.cursor()
            select_query = f"SELECT * FROM accounts WHERE account_number = '{account_number}' AND pin = '{pin}'"
            cursor.execute(select_query)
            account = cursor.fetchone()
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

        elif choice == "3":
            admin_password = input("Enter admin password: ")  # Add admin password here
            if admin_password == "adminpassword":  # Change admin password as needed
                print("Admin Login successful.")
                admin_actions()
            else:
                print("Incorrect admin password.")

        elif choice == "4":
            print("Exiting...")
            display_accounts()  # Display all accounts before exiting
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