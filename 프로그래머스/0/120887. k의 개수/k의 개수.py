def solution(i, j, k):
    answer = 0
    for num in range(i,j+1) :
        for i in str(num):
            if i in str(k) :
                answer += 1

    return answer