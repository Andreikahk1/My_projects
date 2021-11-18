def operation(op):
    if op == "+":
        summ()
        return True
    elif op == "-":
        subt()
        return True
    elif op == "/":
        divi()
        return True
    elif op == "*":
        mult()
        return True
    elif op == "**":
        powr()
        return True
    elif op == "//":
        idiv()        
        return True
    elif op == "%":
        modl()
        return True
    elif op == "exit":
        return False
    else:
        print("Operation is not known.")
        return True

def summ():
    x = float(input("Enter x: "))
    y = float(input("Enter y: "))
    print("Result of addition x+y is:", x+y)

def subt():
    x = float(input("Enter x: "))
    y = float(input("Enter y: "))
    print("Result of substruction x-y is:", x-y)

def divi():
    x = float(input("Enter x: "))
    y = float(input("Enter y: "))
    if y == 0:
        print("Division by 0 is not possible")
        return True
    else:
        print("Result of division x/y is:", x/y)

def mult():
    x = float(input("Enter x: "))
    y = float(input("Enter y: "))
    print("Result of multiplication x*y is:", x*y)
        
def powr():
    x = float(input("Enter x: "))
    y = float(input("Enter power: "))
    print("Result of exponentiation x**y is:", x**y)

def idiv():
    x = float(input("Enter x: "))
    y = float(input("Enter y: "))
    if y == 0:
        print("Division by 0 is not possible")
    else:
        print("Result of division x/y is:", x/y)

def modl():
    x = float(input("Enter x: "))
    y = float(input("Enter y: "))
    print("Result of modulus x % y is:", x%y)

def calc():
    exit_flag = True                
    while exit_flag:
        exit_flag = operation(input("Select operation from the given: + - / * ** // % (or 'exit' to exit): "))

calc()
