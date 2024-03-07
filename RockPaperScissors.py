#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 09:44:20 2024

@author: deva
"""

import random

def winner(player_choice,computer_choice):
    if player_choice == computer_choice:
        print("Tie!")
    elif(player_choice == 'rock' and computer_choice == 'paper') or\
        (player_choice == 'scissor' and computer_choice == 'rock') or\
        (player_choice == 'paper' and computer_choice == 'scissor'):
            print("Computer Wins")
    else:
        print("Player Wins.")
   

while True:
    print("Welcome to Rock, Paper, Scissors game.")
    player_choice = input("Enter players chocice:")
    if player_choice.lower() in ['rock','paper','scissor']:
        pass
    else:
        print("Invalid option. Please enter the correct choice.")
    computer_choice = random.choice(['rock','paper','scissor'])
    print("Computer chooses",computer_choice)
    winner(player_choice,computer_choice)
    flag = input("Do you want to play again?(y/n)")
    if flag != 'y':
        print("Thank you. Come back later")
        break
    elif flag == 'y':
        continue
    else:
        print("Please enter a valid option.")