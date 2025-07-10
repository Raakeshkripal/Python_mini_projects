def calculator(num1,num2,operator):
    if operator == '+':
        result = num1 +num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '/':
        result = num1/num2
    elif operator == '*':
        result = num1*num2
    elif operator == '**':
        result = num1**num2
    else:
        print("invalid operator")
    return result
num1 = float(input("enter the number 1"))
num2 = float(input("enter the number 2"))
operator= input(" enter the operationn to be performed ")
calculation = calculator(num1, num2 , operator )
print("result=",calculation) 
