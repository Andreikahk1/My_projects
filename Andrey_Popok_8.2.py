import sys

class Timer:
    def __init__(self, h, m, s):
        self.__stack_list = []
        try:
            if h > 23 or h < 0 or m > 59 or m < 0 or s > 59 or s < 0:
                raise OverflowError # had no time to create own Error class for wrong timer params, will add in the next version
            else:
                self.__h = int(h)
                self.__m = int(m)
                self.__s = int(s)
        except TypeError:
            print("Incorrect timer params, please enter only digits")
            sys.exit()
        except OverflowError:
            print("Timer value cannot be set")
            sys.exit()
    
    def __str__(self):
        hh = self.two_digits(self.__h)
        mm = self.two_digits(self.__m)
        ss = self.two_digits(self.__s)
        return hh+':'+mm+':'+ss

    def two_digits(self,val):
        s = str(val)
        if len(s) == 1:
            s = '0' + s
        return s
        
    def next_second(self):
        self.__s += 1
        if self.__s == 60:
            self.__s = 0
            self.__m += 1
            if self.__m == 60:
                self.__m = 0
                self.__h += 1
                if self.__h == 24:
                    self.__h = 0
                else:
                    self.__h += 1
            else:
                self.__m += 1        
        else:
            self.__s += 1

    def prev_second(self):
        self.__s -= 1
        if self.__s == -1:
            self.__s = 59
            self.__m -= 1
            if self.__m == -1:
                self.__m = 59
                self.__h -= 1
                if self.__h == -1:
                    self.__h = 23
                else:
                    self.__h -= 1
            else:
                self.__m -= 1        
        else:
            self.__s -= 1
    
def main():

    timer = Timer(23,59,59)
    print(timer)
    timer.next_second()
    print(timer)
    timer.prev_second()
    print(timer)

main()