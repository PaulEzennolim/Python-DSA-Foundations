#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simple Cashpoint (ATM) Simulator
Author: Paul Ezennolim
Date: 10 Oct 2025

This program simulates a very basic ATM machine.
It checks a user's PIN, allows cash withdrawals or mobile top-ups,
and updates the balance accordingly.
"""

# --- Subfunctions ---

def check_PIN(true_pin):
    """
    Ask the user to enter their PIN and verify it.

    The user has up to 3 attempts.
    Returns True if the entered PIN matches the stored PIN.
    Returns False if the user fails after 3 tries.
    """
    attempts = 0
    while attempts < 3:
        entered = input("Please enter your PIN: ").strip()
        if entered == true_pin:
            print("PIN accepted.\n")
            return True  # success
        else:
            attempts += 1
            print(f"Incorrect PIN. Attempts remaining: {3 - attempts}")
    print("Too many incorrect attempts. Card retained.\n")
    return False  # failed after 3 tries


def withdrawal(balance):
    """
    Handle a cash withdrawal.

    Rules:
    - Must be a multiple of £10
    - Maximum of £100 per transaction
    - Cannot exceed current balance
    Returns a tuple: ("withdrawal-request", amount withdrawn)
    """
    try:
        amount = float(input("Enter withdrawal amount (£): "))
    except ValueError:
        # Input was not a valid number
        print("Invalid input — please enter a number.\n")
        return ("withdrawal-request", 0.0)

    # Check conditions
    if amount % 10 != 0:
        print("Amount must be a multiple of £10.\n")
        return ("withdrawal-request", 0.0)
    if amount > 100:
        print("Withdrawal limit is £100 per transaction.\n")
        return ("withdrawal-request", 0.0)
    if amount > balance:
        print("Insufficient funds.\n")
        return ("withdrawal-request", 0.0)

    # Deduct from balance and display results
    new_balance = balance - amount
    print(f"Please take your cash: £{amount:.2f}")
    print(f"Remaining balance: £{new_balance:.2f}\n")
    return ("withdrawal-request", amount)


def mobile_topup(balance):
    """
    Simulate a mobile phone top-up transaction.

    Steps:
    - User enters phone number twice for confirmation
    - Amount must be multiple of £10
    - Amount cannot exceed current balance
    Returns a tuple: ("mobile-topup", amount topped up)
    """
    num1 = input("Enter mobile number: ").strip()
    num2 = input("Re-enter mobile number: ").strip()
    if num1 != num2:
        # Numbers must match for security
        print("Numbers do not match. Transaction cancelled.\n")
        return ("mobile-topup", 0.0)

    try:
        amount = float(input("Enter top-up amount (£): "))
    except ValueError:
        # Non-numeric input
        print("Invalid amount.\n")
        return ("mobile-topup", 0.0)

    if amount % 10 != 0:
        print("Amount must be a multiple of £10.\n")
        return ("mobile-topup", 0.0)
    if amount > balance:
        print("Insufficient balance for top-up.\n")
        return ("mobile-topup", 0.0)

    # Successful top-up
    new_balance = balance - amount
    print(f"£{amount:.2f} top-up successful for {num1}.")
    print(f"Remaining balance: £{new_balance:.2f}\n")
    return ("mobile-topup", amount)


# --- Main function ---

def cashpoint(true_pin, balance):
    """
    Main function controlling the ATM session.

    Displays a simple text menu and routes to the selected operation:
    1. Check balance
    2. Withdraw cash
    3. Mobile top-up
    Returns a string or tuple describing what happened.
    """
    print("Welcome to SimpleCashpoint!\n")

    # Step 1: Verify PIN
    if not check_PIN(true_pin):
        return "PIN-error"  # end session if incorrect

    # Step 2: Display main menu
    print("Select transaction type:")
    print("1. Check balance")
    print("2. Withdraw cash")
    print("3. Mobile top-up")

    choice = input("Enter choice (1–3): ").strip()

    # Step 3: Handle each menu option
    if choice == "1":
        # Balance check
        print(f"Your current balance is £{balance:.2f}\n")
        return "balance-request"

    elif choice == "2":
        # Withdrawal option
        return withdrawal(balance)

    elif choice == "3":
        # Mobile top-up option
        return mobile_topup(balance)

    else:
        # Invalid menu choice
        print("Invalid selection.\n")
        return "invalid-option"


# --- Testing entry point ---
if __name__ == "__main__":
    # Run a sample session for testing purposes
    # PIN is '1234', starting balance is £3415.55
    result = cashpoint("1234", 3415.55)
    print("Function returned:", result)
