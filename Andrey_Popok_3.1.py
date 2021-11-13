hat_list = [1,2,3,4,5]
print(len(hat_list))
rep_num = int(input("Enter the number that will replace the middle number in the list:"))
hat_list[2] = rep_num
hat_list.remove(len(hat_list)-1)
print(len(hat_list))
print(hat_list)