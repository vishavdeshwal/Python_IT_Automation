#!/usr/bin/env python3

def character_frequency(filename):
    # First try
    try:
        f = open(filename)
    except OSError:
        return None
    
    # Now process the file
    characters = {}
    for line in f:
        for char in line:
            characters[char] = characters.get(char, 0) + 1
    f.close()
    return characters