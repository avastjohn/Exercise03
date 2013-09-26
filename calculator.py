#import functions from arthimetic file
from arithmetic import *

# error checking
def check_errors(args, num):
    if len(args) != num:
        print "Your input sucks. Try again."
        return False

    return True

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
        if check_errors(numbers, 2):
            print add(numbers[0],numbers[1])
    elif operator == "-":
        if check_errors(numbers, 2):
            print subtract(numbers[0],numbers[1])
    elif operator == "*":
        if check_errors(numbers, 2):
            print multiply(numbers[0],numbers[1])    
    elif operator == "/":
        if check_errors(numbers, 2):
            print divide(numbers[0],numbers[1])
    elif operator == "square":
        if check_errors(numbers, 1):
            print square(numbers[0])
    elif operator == "cube":
        if check_errors(numbers, 1):
            print cube(numbers[0])
    elif operator == "pow":
        if check_errors(numbers, 2):
            print power(numbers[0],numbers[1])
    elif operator == "mod":
        if check_errors(numbers, 2):
            print mod(numbers[0],numbers[1])        
    else:
        print "Not a valid calculator command. Please try again!"

    # ask for new input
    user_input = raw_input("> ")
    
