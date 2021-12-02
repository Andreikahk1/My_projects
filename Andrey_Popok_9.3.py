class WeekDayError(Exception):
    pass

class Weeker:
    def __init__(self, day):
        self.__day = ''
        if day not in ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']:
            raise WeekDayError
        else:
            self.__day = day
   
    def __str__(self):
        return 'Weekday is '+self.__day

    def add_days(self, n):
        wday_list = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
        for i in range(1,8):
            if self.__day == wday_list[i-1]:
                break
        j = (((n % 7) + i )) % 7        
        self.__day = wday_list[j-1]

    def subtract_days(self, n):
        wday_list = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
        for i in range(1,8):
            if self.__day == wday_list[i-1]:
                break
        j = ((((i+14) - (n % 7))) % 7)
        self.__day = wday_list[j-1]

def main():
    try:
        weekday = Weeker('Mon')
        print(weekday)
        weekday.add_days(15)
        print(weekday)
        weekday.subtract_days(23)
        print(weekday)
        weekday = Weeker('Monday')
    except WeekDayError:
        print('Sorry, I can not serve your request.')

main()
