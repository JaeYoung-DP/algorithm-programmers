from math import factorial as fact

def solution(balls, share):
    n = fact(balls)
    m = fact(share)
    nm = fact(balls-share)
    
    answer = n/(nm*m)
    
    return answer