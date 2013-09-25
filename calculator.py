#import functions from arthimetic file
from arithmetic import *

#get calculator input from user
user_input = raw_input("> ")

#calculator loops until user quits "q"
while user_input != "q":

    # separate input into tokens to break out operator from numbers
    tokens = user_input.split(" ")
    # separate tokens into numbers and operator
    operator = tokens[0]
    numbers = tokens[1:]

    # turn all numbers into integers
    numbers = map(int, numbers)
    
    #uses operator to determine which function to call
    if operator == "+":
        print add(numbers[0],numbers[1])
    elif operator == "-":
        print subtract(numbers[0],numbers[1])
    elif operator == "*":
        print multiply(numbers[0],numbers[1])    
    elif operator == "/":
        print divide(numbers[0],numbers[1])
    elif operator == "square":
        print square(numbers[0])
    elif operator == "cube":
        print cube(numbers[0])
    elif operator == "pow":
        print power(numbers[0],numbers[1])
    elif operator == "mod":
        print mod(numbers[0],numbers[1])        
    else:
        print "Not a valid calculator command. Please try again!"

    # ask for new input
    user_input = raw_input("> ")
    
