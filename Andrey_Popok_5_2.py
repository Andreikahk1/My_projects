def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    else:
        fib1 = 1
        fib2 = 1
        fibn = 0
        for i in range(3,n+1):
            fibn = fib1 + fib2
            fib1 = fib2
            fib2 = fibn
        return fibn

def main():
    
    for i in range(-1,25):
        res = fib(i)
        print("Fib[",i,"] = ",res, sep = '')

main()