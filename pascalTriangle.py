input_num = int(input("Enter the number of rows: "))
list = [] #an empty list
for column in range(input_num+1):
    list.append([])

    list[column].append(1)
    for row in range(1,column):
        list[column].append(list[column-1][row-1] + list[column-1][row])
    if input_num != 0:
        list[column].append(1)
print(list)
