def solution(num, k):
    answer = 0
    str_num = str(num)
    str_k = str(k)
    
    if str_k in str_num:
        answer = str_num.index(str_k) + 1
    else:
        answer -= 1
        
    return answer