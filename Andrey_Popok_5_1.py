def fact(n):
    if n < 0:
        return None
    elif n < 2:
        return 1
    else:
        x = 1
        for i in range(2,n+1):
            x *= i
        return x

def main():
    for i in range(-1,9):
        res = fact(i)
        print(i,"! = ",res, sep = '') 
        
main()        