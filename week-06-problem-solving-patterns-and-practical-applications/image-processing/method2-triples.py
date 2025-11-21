#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 13:28:31 2025

@author: paulezennolim
"""

from pylab import *

# Load the image
img = imread('chick.png')

# Get image dimensions
(rows, cols, d3) = img.shape

# --- METHOD 2: Modify whole RGB pixel triples ---
for i in range(rows):            # Loop over all rows
    for j in range(cols):        # Loop over all columns
        
        # img[i, j] is the *entire RGB triple* for pixel (i, j)
        pixel = img[i, j]        # This gives [R, G, B]

        # Example condition:
        # If the pixel is dark (sum of R+G+B < 1.5), make it black.
        # (1.5 is equivalent to average intensity < 0.5)
        if sum(pixel) < 1.5:
            img[i, j] = (0.0, 0.0, 0.0)   # Set the pixel to black

        # You could instead change the pixel to any other RGB triple.
        # Example: img[i, j] = (1.0, 0.0, 0.0)  # make pixel bright red

# Display the edited image
imshow(img)
show()
