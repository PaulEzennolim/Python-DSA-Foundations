#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 24 2025
@author: paulezennolim

This program implements a Moving Average Filter to smooth
a noisy signal and recover the original 'pure' waveform.

It loads the noisy signal data from 'noisy_signal.txt',
computes a moving average over a specified window size,
and plots both the original noisy and smoothed signals.
"""

import numpy as np
import matplotlib.pyplot as plt


# ---------------------------------------------------------
# 1. Function to load signal data from a text file
# ---------------------------------------------------------
def load_signal(filename):
    """Reads a text file with 1 or 2 columns and returns (x, y)."""
    try:
        x, y = np.loadtxt(filename, unpack=True)
    except ValueError:
        y = np.loadtxt(filename)
        x = np.arange(len(y))
    return x, y


# ---------------------------------------------------------
# 2. Moving Average Filter implementation
# ---------------------------------------------------------
def moving_average(signal, window_size):
    """
    Computes the moving average of 'signal' using a given window size.
    Returns a list of smoothed values (same length as signal).
    """
    smoothed = []  # list to store filtered values
    half_window = window_size // 2  # number of samples before/after center

    for i in range(len(signal)):
        # Define window boundaries
        start = max(0, i - half_window)
        end = min(len(signal), i + half_window + 1)

        # Compute average of this window
        window_values = signal[start:end]
        avg = sum(window_values) / len(window_values)
        smoothed.append(avg)

    return smoothed


# ---------------------------------------------------------
# 3. Load the noisy signal
# ---------------------------------------------------------
x_noisy, noisy_signal = load_signal("noisy_signal.txt")

# ---------------------------------------------------------
# 4. Apply the moving average filter
# ---------------------------------------------------------
window_size = 20  # adjust this to smooth more or less
smoothed_signal = moving_average(noisy_signal, window_size)

# ---------------------------------------------------------
# 5. Plot original vs filtered signals
# ---------------------------------------------------------
plt.figure(figsize=(10, 5))
plt.plot(x_noisy, noisy_signal, color='red', label="Noisy Signal", alpha=0.6)
plt.plot(x_noisy, smoothed_signal, color='blue', label=f"Smoothed (W={window_size})", linewidth=2)
plt.title("Recovering Signal using Moving Average Filter")
plt.xlabel("Time (ms or sample index)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
