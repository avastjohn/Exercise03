"""
    No setup
    repeat forever:
        read input DONE
        tokenize input DONE
        if the first token is 'q', quit DONE
        otherwise decide which math function to call based on the tokens we read
"""
from arithmetic import *

user_input = raw_input("> ")

while user_input != "q":
    # separate input into tokens
    tokens = user_input.split(" ")
    # separate tokens into numbers and operator
    operator = tokens[0]
    numbers = tokens[1:]

    # turn all numbers into integers
    for i in numbers:
        numbers[i] = int(numbers[i]
    
###### This is where we are currently working!! ########

    if tokens[0] == "+":
        print add(tokens[1],tokens[2])
    else:
        print "Nopes"

    user_input = raw_input("> ")