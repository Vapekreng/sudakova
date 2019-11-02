def task2():
    text = input('Введите список: ')
    str_list = text.split()
    int_list = []
    length = len(str_list)
    for i in range(length):
        new_number = int(str_list[i])
        int_list.append(new_number)
    max_number = max(int_list)
    index_of_max_number = int_list.index(max_number)
    return max_number, index_of_max_number

print(task2())
