#!/usr/bin/python3

def add(n1,n2):
    return n1 + n2
    
def multiply(n1,n2):
    return n1 * n2
    
def subtract(n1,n2):
    return n1 - n2
    
def divide(n1,n2):
    return n1 / n2
    
functions = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculate():
    
    num1 = float(input("What's is the first number: "))


    for operator in functions:
        print(operator)
    
    operator_choice = input("Choose an operator: ")
    num2 = int(input("What's the next number: "))
 
    function = functions[operator_choice]
    answer = function(num1,num2)
    print(answer)
    
    repeat = False
    while not repeat:
        calculate_again = input(f"Type 'y' to continue calculation with {answer} or type 'n' to start a new calculation or type 'x' to exit: ")
        if calculate_again =="x":
            print("exit")
            repeat = True
        elif calculate_again == "n":
            calculate()
            print("Start")
        else:
        
            operator_choice = input("Choose an operator: ")
            num3 = float(input("What's the next number: "))
            num1 = answer
            function = functions[operator_choice]
            answer = function(num1,num3)
            print(f"{num1} {operator_choice} {num3}: {answer}")
            
            
calculate()
    
