#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  3 14:02:22 2025

@author: paulezennolim
"""

# test2.py
# Test script for temperature conversion functions

from temperature_converter import *   # import everything from temperature_convert.py

print("Running tests for temperature conversion...\n")

# Test 1: Freezing point of water
c = 0
print(f"{c} °C = {celsius_to_fahrenheit(c)} °F, {celsius_to_kelvin(c)} K")

# Test 2: Boiling point of water
c = 100
print(f"{c} °C = {celsius_to_fahrenheit(c)} °F, {celsius_to_kelvin(c)} K")

# Test 3: Room temperature
c = 25
print(f"{c} °C = {celsius_to_fahrenheit(c)} °F, {celsius_to_kelvin(c)} K")

# Test 4: Negative temperature
c = -40
print(f"{c} °C = {celsius_to_fahrenheit(c)} °F, {celsius_to_kelvin(c)} K")

# Test 5: Random value
c = 273.15
print(f"{c} °C = {celsius_to_fahrenheit(c)} °F, {celsius_to_kelvin(c)} K")
