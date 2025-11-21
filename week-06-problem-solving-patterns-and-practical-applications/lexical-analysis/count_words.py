#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 21 10:54:32 2025

@author: paulezennolim
"""

def readStopWords(filename):
    """
    Read stopwords from file and return as list of strings.
    """
    stops = []
    with open(filename, 'r') as f:
        for line in f:
            stops.append(line.strip())
    return stops


def countWords(filename, stopwords_list):
    """
    Count words in a file, ignoring any that appear in stopwords_list.
    Returns a dictionary:  { word : count }
    """

    counts = {}

    with open(filename, 'r') as f:
        for line in f:
            words = line.split()
            for word in words:
                if word not in stopwords_list:
                    counts[word] = counts.get(word, 1) + (word in counts)

    return counts


def printTop20(counts):
    """
    Given a dictionary of word counts, print the top 20
    words in descending order of frequency.
    """
    sorted_items = sorted(
        counts.items(),
        key=lambda x: x[1],
        reverse=True
    )

    for word, freq in sorted_items[:20]:
        print(f"{word} = {freq}")


def similarity(d1, d2):
    """
    Compute lexical overlap similarity between two word-count dictionaries.
    The score is:
        N / (len(d1) + len(d2) - N)
    where N is the number of shared distinct words.
    """

    # Convert keys to sets of words
    words1 = set(d1.keys())
    words2 = set(d2.keys())

    # Count shared words
    N = len(words1.intersection(words2))

    # Compute denominator
    denom = len(words1) + len(words2) - N

    # Avoid division by zero
    if denom == 0:
        return 0

    return N / denom
