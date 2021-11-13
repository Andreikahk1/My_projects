while True:
    op = input("Select operation from the given: + - / * ** // % (or 'exit' to exit): ")
    if op == "+":
        x = float(input("Enter x: "))
        y = float(input("Enter y: "))
        print("Result of addition x+y is:", x+y)
    elif op == "-":
        x = float(input("Enter x: "))
        y = float(input("Enter y: "))
        print("Result of substruction x-y is:", x-y)
    elif op == "/":
        x = float(input("Enter x: "))
        y = float(input("Enter y: "))
        print("Result of division x/y is:", x/y)
    elif op == "*":
        x = float(input("Enter x: "))
        y = float(input("Enter y: "))
        print("Result of multiplication x*y is:", x*y)
    elif op == "**":
        x = float(input("Enter x: "))
        y = float(input("Enter power: "))
        print("Result of exponentiation x**y is:", x**y)
    elif op == "//":
        x = float(input("Enter x: "))
        y = float(input("Enter y: "))
        print("Result of floor division x//y is:", x//y)
    elif op == "%":
        x = float(input("Enter x: "))
        y = float(input("Enter y: "))
        print("Result of modulus x % y is:", x%y)
    elif op == "exit":
        break
