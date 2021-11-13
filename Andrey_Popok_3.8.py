r_start = int(input("Enter the start of range : "))
r_end = int(input("Enter the end of range : "))
list_num = []
sum = 0
for i in range(r_start,r_end+1):
    if i % 3 == 0:
        list_num.append(int(i))
        sum += i
print("Average is: ",float(sum/len(list_num)))