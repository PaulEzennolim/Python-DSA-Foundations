#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 13:14:36 2025

@author: paulezennolim
"""

from pylab import *

# Load the image
img = imread('chick.png')

# Get image dimensions
# rows = height, cols = width, d3 = number of colour channels (3 for RGB)
(rows, cols, d3) = img.shape

# --- METHOD 1: Modify individual intensity values ---
for i in range(rows):            # Loop over all rows (top to bottom)
    for j in range(cols):        # Loop over all columns (left to right)
        for k in range(d3):      # Loop over each colour channel (R, G, B)

            # img[i, j, k] is a *single numeric intensity* between 0.0 and 1.0
            # Here we invert the colour: low values become high and vice versa
            img[i, j, k] = 1 - img[i, j, k]

            # This is where you could apply ANY pixel-level operation,
            # e.g., thresholding, brightness adjustment, noise, etc.

# Display the edited image
imshow(img)
show()
