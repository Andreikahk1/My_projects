x1 = float(input("Enter number 1: "))
x2 = float(input("Enter number 2: "))
x3 = float(input("Enter number 3: "))
x4 = float(input("Enter number 4: "))
if x1 > x2:
    if x1 > x3:
        if x1 > x4:
            print("Max value is: ",x1)
        else:
            print("Max value is: ",x4)
    elif x3 > x4:
        print("Max value is: ",x3)
    else:
        print("Max value is: ",x4)
elif x2 > x3:
    if x2 > x4:
        print("Max value is: ",x2)
    else:
        print("Max value is: ",x4)
else:
    if x3 > x4:
        print("Max value is: ",x3)
    else:
        print("Max value is: ",x4)                