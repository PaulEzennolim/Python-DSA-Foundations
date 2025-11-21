#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 21 11:04:15 2025

@author: paulezennolim
"""

from count_words import countWords, printTop20, readStopWords, similarity

# load stopwords
stops = readStopWords('stopwords.txt')

# Print counts
print("=== Counting words from mobypara.txt (with stopwords removed) ===")
d = countWords('mobypara.txt', stops)
print(d)

# count words WITH stopwords removed
print("\n=== Top 20 (stopwords removed, mobydick.txt) ===")
counts_no_stop = countWords('mobydick.txt', stops)
printTop20(counts_no_stop)

# count words WITHOUT removing stopwords
print("\n=== Top 20 (all words, mobydick.txt) ===")
counts_all = countWords('mobydick.txt', [])
printTop20(counts_all)

# build dictionaries for each George file
d1 = countWords('george01.txt', stops)
d2 = countWords('george02.txt', stops)
d3 = countWords('george03.txt', stops)
d4 = countWords('george04.txt', stops)

print("\n=== Similarity scores for George files ===")

# compute pairwise similarity
print("01 vs 02:", similarity(d1, d2))
print("01 vs 03:", similarity(d1, d3))
print("01 vs 04:", similarity(d1, d4))
print("02 vs 03:", similarity(d2, d3))
print("02 vs 04:", similarity(d2, d4))
print("03 vs 04:", similarity(d3, d4))
