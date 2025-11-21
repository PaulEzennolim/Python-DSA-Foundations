#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  3 13:51:13 2025

@author: paulezennolim
"""

# distance_converter.py
# Converts distance in miles to kilometers

def miles_to_kilometers(miles):
    """Convert miles to kilometers."""
    return miles * 1.60934   # precise conversion factor

def main():
    try:
        # Ask the user for input
        miles = float(input("Enter distance in miles: "))
        
        # Convert using our function
        kilometers = miles_to_kilometers(miles)
        
        # Print result nicely
        print("\nConverting distance in miles to kilometers...")
        print(f"Distance in miles:      {miles:.2f}")
        print(f"Distance in kilometers: {kilometers:.2f}")
    except ValueError:
        print("Error: Please enter a valid number.")

# Run program only if executed directly
if __name__ == "__main__":
    main()
