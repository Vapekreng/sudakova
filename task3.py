def task3(init_list):
    answer = False
    if (init_list == sorted(init_list)) or (init_list == sorted(init_list, reverse=True)):
        answer = True
    return answer
