def is_prime(value):
    if value >= 2:
        for i in range(2,value):
            if value % i == 0:
                return False
        return True
    else:
        print("This number can not be checked for prime.")
        exit()
print("The result is:",is_prime(int(input("Enter the number > 2 for prime checking: "))))

