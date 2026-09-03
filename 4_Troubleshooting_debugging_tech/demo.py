#!/usr/bin/env python3

def meters_to_miles(meters):
    # 1 mile = 1609.34 meters
    miles = meters / 1609.34
    return miles

# Ask the user for input
meters_input = float(435678987654)

# Convert and display result
miles_output = meters_to_miles(meters_input)
print(f"{meters_input} meters is equal to {miles_output:.4f} miles.")
