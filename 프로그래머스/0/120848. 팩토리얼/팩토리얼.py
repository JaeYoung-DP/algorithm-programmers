def solution(n):
    x = 1
    y = 1
    while x <= n: # 
        y += 1
        x *= y
        
    return y - 1