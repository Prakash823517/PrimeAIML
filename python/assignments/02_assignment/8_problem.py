def calculator(a, b, operation):
    if(operation == '+'):
        return a + b
    elif(operation == '-'):
        return a - b
    elif(operation == '*'):
        return a * b
    elif(operation == '/'):
        if(b == 0):
            return "Can't divide by zero"
        return a / b
    else:
        return "invalid opertor"

print(calculator(2, 4, '*'))
print(calculator(2, 4, '$'))
