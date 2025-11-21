#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 24 13:45:12 2025

@author: paulezennolim
"""

import matplotlib.pyplot as plt

# ---------------------------------------------------------
# 1. Create lists for x and y values
# ---------------------------------------------------------
Xs = []   # List of x values
Ys_f = [] # List of f(x) values
Ys_g = [] # List of g(x) values

# ---------------------------------------------------------
# 2. Compute f(x) = x^2 + 20 and g(x) = (x/2)^3 - 100
# ---------------------------------------------------------
for x in range(21):  # x goes from 0 to 20 (inclusive)
    f = x**2 + 20
    g = (x / 2)**3 - 100
    Xs.append(x)
    Ys_f.append(f)
    Ys_g.append(g)

# ---------------------------------------------------------
# 3. Plot both functions
# ---------------------------------------------------------
plt.figure(figsize=(8, 5))
plt.plot(Xs, Ys_f, label="f(x) = x² + 20", color='blue')
plt.plot(Xs, Ys_g, label="g(x) = (x/2)³ - 100", color='red')

# Add labels and title
plt.title("Plots of f(x) = x² + 20 and g(x) = (x/2)³ - 100")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()

# Display the graph
plt.show()
