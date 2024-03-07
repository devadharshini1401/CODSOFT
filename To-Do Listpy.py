#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 01:39:09 2024

@author: deva
"""

tasks = []
completed_task = []

def add_task():
    task = input("Enter a task to add: ")
    tasks.append(task)
    while True:
        flag = input('Do you wish to add more tasks? (y/n): ')
        if flag == 'y':
            task = input("Enter a task to add: ")
            tasks.append(task)
        elif flag == 'n':
            break
        else:
            print('Enter a valid option')           
            
def view_task(task):
    for index,task in enumerate(task,1):
        print(index,".",task)
        
def update_task():
    num =  int(input("Enter the task number you want to update:"))
    task_no = num - 1
    new_task = input("Enter the new updation:")
    print("\nList after Updation:")
    tasks[task_no] =  new_task
    for index,task in enumerate(tasks,1):
        print(index,".",task)

def complete_task():
    num =  int(input("Enter the task number you want to mark as complete:"))
    task_no = num - 1
    completed_task.append(tasks.pop(task_no))
    print(completed_task)
    print("Incomplete Tasks:")
    view_task(tasks)
    print("Completed Tasks:")
    view_task(completed_task)
    

while True:
    print("\n===============")
    print("Task Tracker:")
    print("===============")
    print("1. Add Task")
    print("2. View Task")
    print("3. Update Task")
    print("4. Complete Task")
    print("5. Exit")
    
    choice = int(input("Choose your option from above:"))

    if choice == 1:
        add_task()
        print("Task Added Successfully.")
    elif choice == 2:
        print("\nList of your pending tasks:")
        print("============================")
        view_task(tasks)
    elif choice == 3:
        update_task()
    elif choice ==4:
        complete_task()
    elif choice == 5:
        print("Thank you! Hope you have a good day ahead!")
        break
    else:
        print("Enter a Valid option.")
