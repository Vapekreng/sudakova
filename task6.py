def task6(init_list):
    while len(init_list) > 1:
        first = max(init_list)
        init_list.remove(first)
        second = max(init_list)
        init_list.remove(second)
        if first != second:
            diff = first - second
            init_list.append(diff)
    return init_list[0]
