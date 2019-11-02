def task4(init_list):
    maximum = 0
    current_value = 0
    length = len(init_list)
    for i in range(length):
        if init_list[i] == 1:
            current_value += 1
            if current_value > maximum:
                maximum = current_value
        else:
            current_value = 0
    return maximum

