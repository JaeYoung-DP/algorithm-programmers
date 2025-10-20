def solution(my_string):
    answer = []
    for i in my_string:
        if i.isdigit():
            answer.append(i)
        else:
            answer.append(' ')
    s = ''.join(answer)


    total = 0
    for i in s.split():
        total += int(i)

    return total