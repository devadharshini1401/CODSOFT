#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 01:16:50 2024

@author: deva
"""
import math
def add(x,y):
    print("Addition:",x+y)
def sub(x,y):
    print("Subtraction:",x-y)
def multi(x,y):
    print("Multiplication:",x*y)
def div(x,y):
    print("Division:",x/y)
def expo(x,y):
    print("Exponentiation:",x ** y)
def sqrt1(x):
    if x>0:
        print("Square root:",math.sqrt(x))
    else:
        print("Square root for a negative number is not valid.")
print("\nSimple Calcualtor")

while True: 
    print("\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exponentiation\n6. Square root\n7. Exit")
    choice = float(input("Enter the operation you want to perform:"))
    if choice == 7:
        print("Thank you.")
        break
    if choice == 6:
        x = float(input("Enter a number:"))
        sqrt1(x)
        continue
    if choice in [1,2,3,4,5]:
        x = float(input('Enter the first number:'))
        y = float(input('Enter the second number:'))
        if choice == 1:
            add(x,y)
        elif choice == 2:
            sub(x, y)
        elif choice == 3:
            multi(x, y)
        elif choice == 4:
            div(x, y)
        elif choice == 5:
            expo(x, y)
    else:
        print("Enter a valid number")