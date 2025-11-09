def solution(arr):
    length = len(arr)
    
    target_length = 1
    while target_length < length:
        target_length *= 2
    zeros = target_length - length
    
    # 0을 추가한 결과 배열 생성
    result = arr + [0] * zeros
    
    return result