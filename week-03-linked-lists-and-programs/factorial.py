#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 13:37:45 2025

@author: paulezennolim
"""
def factorial(n):
    fact = 1
    while n > 0:
        fact = fact * n
        n = n - 1
    return fact

