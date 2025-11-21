#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 13:34:14 2025

@author: paulezennolim
"""
from pylab import *

img = imread('che.png')       # Load the greyscale Che image
img = img.astype(float32)     # Ensure numeric type

print("Original image shape:", img.shape)
(rows, cols, d3) = img.shape   # d3 = 3 (R,G,B identical in greyscale images)

# Make a working copy so original stays unchanged
img1 = array(img)



# =============================================================
# STRONGLY MONOCHROME (BLACK AND WHITE)
# Method 1: modify individual intensities
# Rule: intensity < 0.5 → 0.0 else → 1.0
# =============================================================

def effect_monochrome(img):
    out = array(img)            # work on a copy
    (rows, cols, d3) = out.shape
    print("Applying Effect 1: Black & White (monochrome)")

    for i in range(rows):
        for j in range(cols):
            for k in range(d3):     # each R,G,B value (same for greyscale)
                if out[i, j, k] < 0.5:
                    out[i, j, k] = 0.0
                else:
                    out[i, j, k] = 1.0

    return out



# =============================================================
# BLACK AND RED VERSION
# Method 2: modify whole pixel triples
# Dark pixels → black
# Light pixels → red (1, 0, 0)
# =============================================================

def effect_black_red(img):
    out = array(img)
    (rows, cols, d3) = out.shape
    print("Applying Effect 2: Black & Red")

    for i in range(rows):
        for j in range(cols):

            pixel = out[i, j]   # full RGB triple
            if sum(pixel) < 1.5:       # dark pixel
                out[i, j] = (0.0, 0.0, 0.0)
            else:
                out[i, j] = (1.0, 0.0, 0.0)   # bright red

    return out



# =============================================================
# RED BACKGROUND + BLACK FACE INSIDE CHE'S FACE AREA
# Method 2
#
# We approximate the face region with a rectangle:
#   These values depend on the actual che.png dimensions.
# -------------------------------------------------------------
# You may adjust row_min,row_max,col_min,col_max depending on
# your copy of the che image — but the logic stays the same.
# =============================================================

def effect_red_background_black_face(img):
    out = array(img)
    (rows, cols, d3) = out.shape
    print("Applying Effect 3: Red background / Black face")

    # APPROX face bounding box (adjust if needed)
    row_min, row_max = int(rows*0.15), int(rows*0.75)
    col_min, col_max = int(cols*0.25), int(cols*0.75)

    for i in range(rows):
        for j in range(cols):

            pixel = out[i, j]
            dark = sum(pixel) < 1.5

            inside_face = (row_min <= i <= row_max) and (col_min <= j <= col_max)

            if inside_face:
                # inside Che's face area
                if dark:
                    out[i, j] = (0.0, 0.0, 0.0)   # black
                else:
                    out[i, j] = (1.0, 0.0, 0.0)   # red
            else:
                # outside face = fully red poster background
                out[i, j] = (1.0, 0.0, 0.0)

    return out



# =============================================================
# FUNKY CHE
# Using 3-colour mapping:
#   intensity > 0.66  → red
#   intensity < 0.33  → blue
#   otherwise         → green
# Method 2
# =============================================================

def effect_funky(img):
    out = array(img)
    (rows, cols, d3) = out.shape
    print("Applying Effect 4: Funky Che (RGB threshold colouring)")

    for i in range(rows):
        for j in range(cols):

            px = out[i, j]
            avg = sum(px) / 3.0      # intensity average (all channels equal)

            if avg > 0.66:
                out[i, j] = (1.0, 0.0, 0.0)    # red
            elif avg < 0.33:
                out[i, j] = (0.0, 0.0, 1.0)    # blue
            else:
                out[i, j] = (0.0, 1.0, 0.0)    # green

    return out



# =============================================================
# OVERLAY THE CHICK IMAGE ONTO THE CHE IMAGE
# The chick image is smaller; place it on Che.
#
# Steps:
# 1. Load chick.png
# 2. For each pixel in chick, copy to Che's location.
# Method 2 is used (replace entire pixel at once).
# =============================================================

def effect_overlay_chick(img):
    print("Applying Effect 5: Overlay chick onto Che")

    che = array(img)
    chick = imread('chick.png')
    chick = chick.astype(float32)

    (r_che, c_che, _) = che.shape
    (r_ch, c_ch, _) = chick.shape

    # Place chick in top-left corner (can be changed)
    for i in range(r_ch):
        for j in range(c_ch):
            che[i, j] = chick[i, j]

    return che

# Uncomment ONE of the following lines to test each effect.

# result = effect_monochrome(img1)
# result = effect_black_red(img1)
# result = effect_red_background_black_face(img1)
# result = effect_funky(img1)
# result = effect_overlay_chick(img1)

imshow(result)
show()

