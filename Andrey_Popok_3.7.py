s = input("Enter the list of numbers into a single line divided by blanks: ")
li1 = s.split(" ")
list_num = []
sum = 0
for i in range(len(li1)):
    if li1[i].isdigit:
        list_num.append(int(li1[i]))
        sum += list_num[i]
print("Average value of given numbers is: ",float(sum/len(list_num)))