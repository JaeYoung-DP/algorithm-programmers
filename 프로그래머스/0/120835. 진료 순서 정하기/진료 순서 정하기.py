def solution(emergency):
    answer = []
    sorted_emergency = sorted(emergency, reverse = True) #큰값부터 아래로 (내림차순)
    for i in emergency: 
        answer.append(sorted_emergency.index(i) + 1)
        
    return answer

