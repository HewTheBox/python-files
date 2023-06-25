def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

num1 = int(input("What's the first number?: "))

for signs in operations:
    print(signs)

operation_symbol = input("Pick an operation from the line above: ")

num2= int(input("What's the second number?: "))

calculation_function = operations[operation_symbol]
answer1 = calculation_function(num1,num2)
print(answer1)
go_again = True
while go_again:

    for signs in operations:
        print(signs)
    operation_symbol = input("pick another operation")

    num3 = int(input("Enter  the next number? "))
    calculation_function = operations[operation_symbol]
    answer2 = answer1
    answer2 += calculation_function(answer1,num3)
    print(f"{answer1} {operation_symbol} {num3} = {answer2}")

    run_again = input("type 'y' to continue or any other character to exit? ")
    if run_again !="y":
        go_again = False








# def action():
    
#     sign = operations[operation_symbol]

#     if sign =="+":
#         return add(num1,num2)
#     elif sign =="-":
#         return subtract(num1,num2)
#     elif sign == "*":
#         return multiply(num1,num2)
#     elif sign =="/":
#         return divide(num1,num2)
#     else:
#         return "Wrong input"
        

# answer = action()
# print(answer)