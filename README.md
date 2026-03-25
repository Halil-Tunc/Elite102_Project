# AccountKeeper

A Python banking simulation project built with MySQL as part of Code2College. This project allows users to create accounts, log in, deposit money, withdraw money, change their PIN, and access simple admin tools.

## Overview

AccountKeeper is one of my early SQL-based Python projects. I built it to practice connecting Python to a MySQL database and performing account-related actions through a command-line interface.

## Features

- Create a bank account with an account number and PIN
- Log in to an existing account
- Deposit money
- Withdraw money
- Change an account PIN
- Admin login with extra account management options
- MySQL database integration

## Tech Stack

- Python
- MySQL
- `mysql-connector-python`
- Poetry

## How It Works

When the program starts, the user can:
1. Create an account
2. Log in
3. Use the admin login
4. Exit

After logging in, a user can:
- deposit money
- withdraw money
- change their PIN
- log out

The admin menu includes:
- viewing all accounts
- changing the PIN of an account
- returning to the main menu

## Files

- `main.py` - main banking system logic
- `pyproject.toml` - project configuration
- `poetry.lock` - dependency lock file
- `.replit` - Replit configuration

## Running the Project

Before running the project, make sure you have:
- Python installed
- MySQL installed and running
- a database named `bank`
- a table named `accounts`

Then install the required dependency and run:

```bash
python main.py
