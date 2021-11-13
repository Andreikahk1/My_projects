c0 = int(input("Enter any positive non-zero integer: "))
while (c0 != 1):
    if (c0 % 2) == 0:
        c0 = int(c0/2)
    else:
        c0 = int(3*c0 + 1)
    print(c0)