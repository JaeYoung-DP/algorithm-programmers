def solution(rsp):
    answer = ''
    for game in rsp:
        if game == "2" : 
            answer +="0"
        elif game == "0":
            answer +="5"
        else:
            answer +="2"
            
    return answer