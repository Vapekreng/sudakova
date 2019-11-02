def task1(text, first, second):
    words = text.split()
    answer = []
    while (FIRST in words) and (SECOND in words):
        first_index = words.index(FIRST)
        second_index = words.index(SECOND)
        third_index = second_index + 1
        if (first_index == second_index - 1) and (third_index < len(words)):
            answer.append(words[third_index])
            words.pop(third_index)
            words.pop(second_index)
            words.pop(first_index)
        else:
            minimum_index = min(first_index, second_index)
            words.pop(minimum_index)
    return answer
