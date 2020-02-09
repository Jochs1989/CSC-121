# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 13:26:55 2020

This program will find the two largest numbers
01/27/2020
CSC-121 M1HW2–Nested Statements
Jeffrey Ochs
"""

# Lets the user set the variables for the amount of numbers they enter and sets the largest number
loopAmount = int(input("How many numbers are you going to enter? > "))
largestNumber = int(input("Please enter a number: "))
# Assigns the secondlargest number to zero for validation so the program doesn't crash
secondLargest = 0
# Loops the program for however many numbers the user wanted.
for counter in range(1,loopAmount):
    number = int(input("Please enter a number: "))
    # Assigns the users entry as either largest number or second largest number. otherwise leaves the if statement.
    if number > largestNumber:
        secondLargest = largestNumber
        largestNumber = number
    elif number > secondLargest:
        secondLargest = number
        

print("\nThe largest number is: " + str(largestNumber) + ".\nThe second largest number is: " + str(secondLargest))