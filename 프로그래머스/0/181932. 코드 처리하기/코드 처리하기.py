def solution(code):
    result = ""
    mode = False # 0을 나타냄
    
    for idx, i in enumerate(code):
        if i == "1":
            mode = not mode
            continue
        if not mode and idx%2==0:
            result +=i
        elif mode and idx%2==1:
            result +=i
    
    if not result:
        return "EMPTY"
        
    return result