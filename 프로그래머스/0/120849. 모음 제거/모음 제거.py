def solution(my_string):
    answer = ''
    delete = ["a", "e", "i", "o", "u"]
    
    for i in my_string:
        if i not in delete:
            answer +=i
    return answer