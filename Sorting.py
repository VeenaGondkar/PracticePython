num_list = [23, 34, 10, 5, 4, 6, 14, 11, 1, 20, 16, 2, 26]
a = 0

for passnum in range(len(num_list) - 1, 0, -1):
    for i in range(passnum):
        if (num_list[i] > num_list[i+1]):
            temp = num_list[i]
            num_list[i] = num_list[i+1]
            num_list[i+1] = temp
            print(num_list)
            print("-------------------------------------")

print("The final sorted list is ")
print(num_list)