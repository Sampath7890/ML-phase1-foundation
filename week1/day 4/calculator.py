"""
Rebuild your Day 1 calculator using functions
Write separate functions: add(a,b), subtract(a,b), multiply(a,b), divide(a,b)
divide should handle division by zero — return "Error: cannot divide by zero"
Write a main calculate(a, op, b) function that calls the right one based on op (+,-,*,/)
calculate(10, "+", 5) → 15
calculate(10, "/", 0) → "Error: cannot divide by zero"
"""
def add(a,b) :
    result = a+b
    return result

def subtract(a,b) :
    result = a - b 
    return result

def multiplication(a,b) :
    result = a * b 
    return result

def division(a,b) :
    if b == 0:
        return "error cannot divide by zer0"
    else :
        return a/b

def calculate(a,op,b) :
    match op :
        case "+" :
            return add(a,b)
        
        case "-" :
            return subtract(a,b)
        
        case "*" :
            return multiplication(a,b)
        
        case "/" :
            return division(a,b)
        
        
    
a = int(input("enter a number:"))
op = input("enter operator (+ , - , * , / ): ")
b = int(input("enter a number:"))

result = calculate(a,op,b)

print(f"{a} {op} {b} = {result}")