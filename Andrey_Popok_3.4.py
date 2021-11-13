list = [1,2,4,4,1,4,2,6,2,9]
print(list)    
list.sort()
flag = True
while flag:
    flag = False
    if len(list) >=2:
        for i in range(len(list)-1):
            if list[i] == list[i+1]:
                del list[i+1]
                flag = True
                break       
print(list)
