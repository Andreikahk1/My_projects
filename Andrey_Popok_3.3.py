list_num = int(input("Please enter how many numbers you want to add: "))
list = []
for i in range(list_num):
    list.append(int(input("Enter the number: ")))
print(list)    
sort_type = input("Please choose sort type: 'asc'(ascending) or 'desc'(descending): ")
flag = True
if sort_type == 'asc':
    while flag:
        flag = False
        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                flag = True
                list[i], list[i+1] = list[i+1], list[i]
else:
    while flag:
        flag = False
        for i in range(len(list)-1):
            if list[i] < list[i+1]:
                flag = True
                list[i], list[i+1] = list[i+1], list[i]
print(list)
