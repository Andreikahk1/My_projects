s = input("Enter the list of numbers into a single line divided by blanks: ")
li1 = s.split(" ")
list_num = []
print("Your input after split:",li1)
for i in range(len(li1)):
    if li1[i].isdigit:
        list_num.append(int(li1[i]))
print("Your input after append:",list_num)
sum = 0
for i in list_num:
    sum += i
print("Sum(list):",sum)
