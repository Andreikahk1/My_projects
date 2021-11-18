def is_year_leap(year):
    if((year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)):   
        return True
    else:  
        return False

def days_of_year(year,month,day):
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if month > 12 or month <1 or year < 1582 or day < 1 or day > 31:
        return None
    else:
        res = 0
        for i in range(month-1):
            res += days[i]
        if month > 2 and is_year_leap(year):
            res += 1
        return res+day
    
test_years = [2000,2007,2013,2020]    
test_months = [12,11,5,2]
test_days = [31,12,6,29]
test_results = [366,316,126,60]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    dy = test_days[i]
    print(yr,mo,dy,"->",end=" ")
    result = days_of_year(yr,mo,dy)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")