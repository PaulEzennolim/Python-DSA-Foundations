#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 13:51:52 2025

@author: paulezennolim
"""
def MySqrt(A):
    """
    Compute the square root of A using Newton's method.
    """
    # Step 1: Initial approximation and error tolerance
    x = 1.0
    errorTolerance = 0.001
    
    # Step 2: Repeat until the approximation is close enough
    while abs(x * x - A) >= errorTolerance:
        # Print current approximation (for debugging)
        print(f"Current approximation: {x}")
        
        # Step 3: Update x using Newton's formula
        x = x - (x * x - A) / (2 * x)
    
    # Step 4: Return the final approximation
    return x

def MyCubeRoot(A):
    """
    Compute the cube root of A using Newton's method.
    """
    x = 1.0
    errorTolerance = 0.001

    while abs(x ** 3 - A) >= errorTolerance:
        print(f"Current approximation: {x}")
        x = x - (x ** 3 - A) / (3 * x * x)
    
    return x
