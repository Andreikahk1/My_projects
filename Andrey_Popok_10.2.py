from os import sep, strerror

class AlphaCounter:
    def __init__(self, filename):
        self.__filename = filename
        self.__filename_hist = filename + '.hist'
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

    def dict_sort(self):
        # solution with sorting using lamda was found on StackOverFlow =((
        self.__counter = {k: v for k, v in sorted(self.__counter.items(), key=lambda item: item[1], reverse=True)}
    
    def write_hist(self):
        try:
            f = open(self.__filename_hist,'wt')
            for key,value in self.__counter.items():
                if value != 0:
                    f.write(str(key)+" -> "+str(value)+"\n")
            f.close()
        except IOError as e:
            print("I/O error occured", e.errno)
        
def main():

    alphacounter = AlphaCounter(input("Please enter the full path to filename: "))
    alphacounter.calc_chars()
    alphacounter.dict_sort()
    alphacounter.print_hist()
    alphacounter.write_hist()

main()
