""" This is a Python program which describes 1 approach to solve the given Problem Statement:
Write a function greet_me() to take your name as input from the command line and print apersonalized greeting like 
"Hello, Rani, how are you today?"
"""
def greet_me( person_name ):
    print("Hello," + person_name + ", How are you today?")

name = input("Enter your name")
greet_me(name)
