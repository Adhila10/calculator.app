# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: division by zero"
    else:
        return a / b


def square_root(a):
    import math
    return math.sqrt(a)

def power(a):
    return a**2



num1 = int(input("Enter num1"))
num2 = int(input("Enter num2"))

print(f"{num1} + {num2} = {add(num1, num2)}")
print(f"{num1} - {num2} = {subtract(num1, num2)}")
print(f"{num1} * {num2} = {multiply(num1, num2)}")
print(f"{num1} / {num2} = {divide(num1, num2)}")
print(f"square root = {square_root(num1)}")
print(f"Power = {power(num1)}")