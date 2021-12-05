from os import strerror

class AlphaCounter:
    def __init__(self, filename):
        self.__filename = filename
        self.__counter = {chr(ch):0 for ch in range(ord('a'),ord('z')+1)}
   
    def calc_chars(self):
        try:
            f = open(self.__filename,'rb')
            data = bytearray(f.read())
            f.close()
            for ch in data:
                if (chr(ch).lower()).isalpha():
                    self.__counter[chr(ch).lower()] += 1
        except IOError as e:
            print("I/O error occured", e.errno)
    
    def print_hist(self):
        for key,value in self.__counter.items():
            if value != 0:
                print(key,' -> ',value)

def main():

    alphacounter = AlphaCounter(input("Please enter the full path to filename: "))
    alphacounter.calc_chars()
    alphacounter.print_hist()

main()
