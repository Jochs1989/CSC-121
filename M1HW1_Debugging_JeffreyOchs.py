# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 13:05:48 2020

This will create a table of squares and cubed numbers
01/27/2020
CSC121M1HW1-Degbugging
Jeffrey Ochs
"""

# Asks the user how many times they would like to the program to loop
loopAmount = int(input("How many times would you like to Square/Cube the number? > "))

# Prints headers for better visuals for the user
print(f'{"Number":<10}{"Square":<10}{"Cube":<10}')
print("---------------------------")
# Loops the program however many times the user asked previously and prints the data
for counter in range(loopAmount+1):
    print(f'{counter:<10}{counter ** 2:<10}{counter ** 3:<10}')
