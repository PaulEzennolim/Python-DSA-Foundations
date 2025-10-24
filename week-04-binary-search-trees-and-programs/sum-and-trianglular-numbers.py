#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 24 13:23:57 2025

@author: paulezennolim
"""

# Function to compute the sum of a list of numbers using a for-loop
def sum_list(numbers):
    total = 0  # Initialize the running total
    for num in numbers:  # Loop through each element in the list
        total += num     # Add each number to the total
    return total  # Return the computed sum


# Function to compute the nth triangular number using a for-loop
def triangular_number(n):
    total = 0  # Initialize the sum
    for i in range(1, n + 1):  # Loop from 1 up to n (inclusive)
        total += i  # Add each integer to the total
    return total  # Return the triangular number


# --- Example usage ---
print(sum_list([3, 4, 5]))   # Output: 12
print(triangular_number(5))  # Output: 15 (5 + 4 + 3 + 2 + 1)

# Function to return a new list with squares of each number in the original list
def square_list(numbers):
    new_list = list(numbers)  # Make a copy to avoid changing the original list
    for i in range(len(new_list)):
        new_list[i] = new_list[i] ** 2  # Square each element
    return new_list


# Function to return a new list with triangular numbers of each number in the original list
def triangular_list(numbers):
    new_list = list(numbers)  # Copy the original list
    for i in range(len(new_list)):
        new_list[i] = triangular_number(new_list[i])  # Use the function defined earlier
    return new_list


# --- Example usage ---
x = [3, 4, 5]
print("Original list:", x)
print("Squared list:", square_list(x))       # Output: [9, 16, 25]
print("Triangular list:", triangular_list(x))  # Output: [6, 10, 15]
print("Original list after function calls:", x)  # Should still be [3, 4, 5]