#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  3 14:04:32 2025

@author: paulezennolim
"""

from distance_converter import * # import everything from distance_converter.py 

print("Running tests for distance conversion...\n")

# Test 1: Zero miles
m = 0
print(f"{m} miles = {miles_to_kilometers(m):.2f} km")

# Test 2: One mile
m = 1
print(f"{m} mile = {miles_to_kilometers(m):.2f} km")

# Test 3: A marathon (26.2 miles)
m = 26.2
print(f"{m} miles = {miles_to_kilometers(m):.2f} km")

# Test 4: Long distance (100 miles)
m = 100
print(f"{m} miles = {miles_to_kilometers(m):.2f} km")

# Test 5: Random value (234 miles)
m = 234
print(f"{m} miles = {miles_to_kilometers(m):.2f} km")