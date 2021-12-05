from os import strerror
import sys
import collections

class Students:
    def __init__(self, filename = "c:\student_data.txt"):
        self.__filename = filename
        self.__students_lst = {}
   
    def load_data(self):
        try:
            with open(self.__filename, 'rt', encoding='UTF-8') as file:
                while (line := file.readline().strip()):
                    fname = line[0:line.find(' ')].strip()
                    line = line[line.find(' '):len(line)].strip()
                    lname = line[0:line.find(' ')].strip()
                    line = line[line.find(' '):len(line)].strip()
                    try:
                        score = float(line.strip())
                        student = fname+' '+lname
                        if student in self.__students_lst:
                            self.__students_lst[student] = float(self.__students_lst[student]) + float(score)
                        else:
                            self.__students_lst[student] = score
                    except ValueError:
                        print("Wrong line has been read from the file. Programm terminated.")
                        sys.exit()

        except IOError as e:
            print("I/O error occured. Programm terminated.", e.errno)
            sys.exit()
    
    def sort_data(self):
        self.__students_lst = collections.OrderedDict(sorted(self.__students_lst.items()))

    def print_data(self):
        for key,value in self.__students_lst.items():
           if value != 0:
              print(key,' : ',value)

        
def main():

    students = Students(input("Enter student's data filename: "))
#    students = Students()
    students.load_data()
    students.sort_data()
    students.print_data()

main()
