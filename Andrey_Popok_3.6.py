s = input("Enter the list of numbers into a single line divided by blanks: ")
li1 = s.split(" ")
list_num = []
for i in range(len(li1)):
    if li1[i].isdigit:
        list_num.append(int(li1[i]))
list_num.sort()
dupl_nums = []
if len(list_num) >=2:
    for i in range(len(list_num)-1):
        if list_num[i] == list_num[i+1]:
            if list_num[i] not in dupl_nums:
                dupl_nums.append(list_num[i])
print(dupl_nums)