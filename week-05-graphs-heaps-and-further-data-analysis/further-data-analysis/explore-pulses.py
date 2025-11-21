#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 13:13:59 2025

@author: paulezennolim
"""

# ==========================================
# Finding Patterns in Data
# ==========================================

# Import necessary libraries
import matplotlib.pyplot as plt
import statistics as stats


# ------------------------------------------
# Step 1: Load the data from the file
# ------------------------------------------
filename = "pulse_data.txt"

# Read all numeric values into a list
with open(filename, "r") as f:
    data = [float(line.strip()) for line in f]

print(f"Loaded {len(data)} data points from {filename}")

# ------------------------------------------
# Step 2: Plot the raw (unsorted) data
# ------------------------------------------
plt.figure(figsize=(10, 4))
plt.plot(data)
plt.title("Pulse Intensities (Original Order)")
plt.xlabel("Observation Index")
plt.ylabel("Intensity")
plt.grid(True)
plt.tight_layout()
plt.show()

# ------------------------------------------
# Step 3: Sort the data and plot again
# ------------------------------------------
data.sort()

plt.figure(figsize=(10, 4))
plt.plot(data)
plt.title("Sorted Pulse Intensities")
plt.xlabel("Index (Sorted Order)")
plt.ylabel("Intensity")
plt.grid(True)
plt.tight_layout()
plt.show()

# ------------------------------------------
# Step 4: (Optional) Plot histogram
# ------------------------------------------
plt.figure(figsize=(8, 4))
plt.hist(data, bins=50, color='skyblue', edgecolor='black')
plt.title("Histogram of Pulse Intensities")
plt.xlabel("Intensity Value")
plt.ylabel("Frequency")
plt.grid(True)
plt.tight_layout()
plt.show()

# ------------------------------------------
# Step 5: (Optional) Print basic statistics
# ------------------------------------------
mean_val = stats.mean(data)
median_val = stats.median(data)
stdev_val = stats.stdev(data)

print(f"Mean Intensity: {mean_val:.4f}")
print(f"Median Intensity: {median_val:.4f}")
print(f"Standard Deviation: {stdev_val:.4f}")
