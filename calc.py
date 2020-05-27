# calculator.py

import math 

def calcInput():
    a = input("Enter the first number: ")
    b = input("Enter the second number: ")
    a = int(a)
    b = int(b)
    print("The number you entered is {} and {}".format(a, b))
    return a, b

def add(a, b):
    print("Add")
    answer = a + b
    print("{} + {} = {}".format(a, b, answer))
    print("Finished")
    return answer
    
def subtract(a, b):
    print("Subtract")
    answer = a - b
    print("{} - {} = {}".format(a, b, answer))
    print("Finished")
    return answer
    
def multiply(a, b):
    print("Multiply")
    answer = a * b
    print("{} * {} = {}".format(a, b, answer))
    print("Finished")
    return answer
    
def divide(a, b):
    print("Divide")
    answer = a / b
    print("{} / {} = {}".format(a, b, answer))
    print("Finished")
    return answer
	
def squareRoot(a):
	print("Square Root")
	answer = math.sqrt(a)
	print("Square root of {} is {}".format(a, answer))

def mathCommand(a, b):
    c = input("Enter a command: ")
    if c == 'a':
        add(a, b)
    elif c == 's':
        subtract(a, b)
    elif c == 'm':
        multiply(a, b)
    elif c == 'd':
        divide(a, b)
    elif c == 'q':
    	squareRoot(a)
    else:
        print("Error: Not a valid command")

if __name__ == "__main__":
	x, y = calcInput()
	mathCommand(x, y)
	print("finished")