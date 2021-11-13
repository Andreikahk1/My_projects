Year = int(input("Enter the year for checking: "))
if((Year % 400 == 0) or (Year % 100 != 0) and (Year % 4 == 0)):   
    print(Year,"is a leap year") 
else:  
    print (Year,"is a common year")  
