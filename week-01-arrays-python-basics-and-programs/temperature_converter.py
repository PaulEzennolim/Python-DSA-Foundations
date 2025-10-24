#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  3 13:57:33 2025

@author: paulezennolim
"""

# temperature_converter.py
# Converts temperature from Celsius to Fahrenheit and Kelvin

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin."""
    return celsius + 273.15

def main():
    try:
        # Ask user for input
        celsius = float(input("Enter temperature in Celsius: "))
        
        # Convert using functions
        fahrenheit = celsius_to_fahrenheit(celsius)
        kelvin = celsius_to_kelvin(celsius)
        
        # Print results
        print("\nConverting temperature from Celsius...")
        print(f"Celsius:    {celsius:.2f} °C")
        print(f"Fahrenheit:{fahrenheit:.2f} °F")
        print(f"Kelvin:    {kelvin:.2f} K")
    
    except ValueError:
        print("Error: Please enter a valid number.")

# Run program only if executed directly
if __name__ == "__main__":
    main()
