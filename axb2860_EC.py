
# Function to convert the given simple algebraic expression into RPN
def exp_to_rpn(text):
    expression = text.rsplit()
    numbers = ""
    operators = ""
    for operator in expression:
        if operator in ['+', '-', '*', '/', '%']:
            operators = operator+" "+operators

        else:
            numbers = numbers+" "+operator

    result = numbers + " "+operators
    print(result)
    print(rpn(result))

# Function to evaluate the RPN expression
def rpn(text):
    expression = text.rsplit()
    stack = []
    # implemented the modulo division
    for operator in expression:
        if operator in ['+', '-', '*', '/', '%']:
            x = stack.pop()
            y = stack.pop()
            if operator == '+':
                result = x+y
            if operator == '-':
                result = y-x
            if operator == '*':
                result = x*y
            if operator == '/':
                result = y/x
            if operator == '%':
                result = y%x
            stack.append(int (result))
        else:
            stack.append(int(operator))
    return (stack.pop())

# input from file

file = open("input_RPN_EC.txt","r")
lines=file.read()

for line in lines.split("\n"):
    exp_to_rpn(line)
