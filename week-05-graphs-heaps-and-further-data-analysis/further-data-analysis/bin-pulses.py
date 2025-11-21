#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 13:20:30 2025

@author: paulezennolim
"""
# ==========================================
#  Data Binning for Histogram Plotting
# ==========================================

import matplotlib.pyplot as plt

# ------------------------------------------
# Step 1: Load data
# ------------------------------------------
filename = "pulse_data.txt"

with open(filename, "r") as f:
    data = [float(line.strip()) for line in f]

print(f"Loaded {len(data)} data points")

# ------------------------------------------
# Step 2: Compute min, max, and value span
# ------------------------------------------
minval = min(data)
maxval = max(data)
vspan = maxval - minval

print(f"Min value = {minval:.4f}, Max value = {maxval:.4f}, Span = {vspan:.4f}")

# ------------------------------------------
# Step 3: Define number of bins and initialize count list
# ------------------------------------------
BINS = 50
counts = [0] * BINS

# ------------------------------------------
# Step 4: Assign each data point to a bin
# ------------------------------------------
for value in data:
    # compute proportional position in value range
    bind = int(BINS * (value - minval) / vspan)
    
    # ensure the maximum value is included in the last bin
    if bind == BINS:
        bind = BINS - 1
    
    # increment the count for that bin
    counts[bind] += 1

# ------------------------------------------
# Step 5: Plot the binned counts
# ------------------------------------------
plt.figure(figsize=(10, 4))
plt.plot(range(BINS), counts, marker='o', linestyle='-', color='teal')
plt.title(f"Histogram via Manual Binning (BINS = {BINS})")
plt.xlabel("Bin Index")
plt.ylabel("Count")
plt.grid(True)
plt.tight_layout()
plt.show()

# ------------------------------------------
# Step 6: Optional – Compare with Matplotlib’s histogram
# ------------------------------------------
plt.figure(figsize=(8, 4))
plt.hist(data, bins=BINS, color='skyblue', edgecolor='black')
plt.title("Comparison: Matplotlib Histogram")
plt.xlabel("Intensity Value")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()
