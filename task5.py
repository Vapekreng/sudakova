def task5(init_list):
    first_row = 'qwertyuiop'
    second_row = 'asdfghjkl'
    third_row = 'zxcvbnm'
    answer = []
    length = len(init_list)
    for i in range(length):
        current_word = init_list[i]
        current_word = current_word.lower()
        symbols_by_rows = [0, 0, 0]
        for symbol in current_word:
            if symbol in first_row:
                symbols_by_rows[0] += 1
            elif symbol in second_row:
                symbols_by_rows[1] += 1
            else:
                symbols_by_rows[2] += 1
        if len(current_word) == max(symbols_by_rows):
            answer.append(init_list[i])
    return answer


