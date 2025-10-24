#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 24 2025
@author: paulezennolim

This program reads four signal text files:
- pure_signal.txt     : original clean signal
- random_noise.txt    : random background noise
- mains_noise.txt     : periodic mains interference (e.g. 50/60 Hz)
- noisy_signal.txt    : combined noisy signal
and plots them for visual comparison.

It handles both one-column (amplitude only) and
two-column (time + amplitude) text file formats.
"""

import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# 1. Load signals safely (handles both 1 or 2 columns)
# ---------------------------------------------------------
def load_signal(filename):
    """Reads a text file and returns (x, y) arrays."""
    try:
        # Try to read as two columns (e.g., time and amplitude)
        x, y = np.loadtxt(filename, unpack=True)
    except ValueError:
        # If only one column, create x as sample index
        y = np.loadtxt(filename)
        x = np.arange(len(y))
    return x, y


# Load all signals
x_pure, pure_signal = load_signal("pure_signal.txt")
x_random, random_noise = load_signal("random_noise.txt")
x_mains, mains_noise = load_signal("mains_noise.txt")
x_noisy, noisy_signal = load_signal("noisy_signal.txt")

# ---------------------------------------------------------
# 2. Plot all signals
# ---------------------------------------------------------
plt.figure(figsize=(10, 8))

plt.subplot(4, 1, 1)
plt.plot(x_pure, pure_signal, color='green')
plt.title("Pure Signal")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(4, 1, 2)
plt.plot(x_random, random_noise, color='gray')
plt.title("Random Noise")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(4, 1, 3)
plt.plot(x_mains, mains_noise, color='orange')
plt.title("Mains Noise (50/60 Hz)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(4, 1, 4)
plt.plot(x_noisy, noisy_signal, color='red')
plt.title("Noisy Signal (Pure + Noise)")
plt.xlabel("Sample or Time")
plt.ylabel("Amplitude")
plt.grid(True)

plt.tight_layout()
plt.show()
