def solution(s):
    unique_chars = []
    for i in s:
        if s.count(i) == 1:
            unique_chars.append(i)
    
    # 4. 리스트를 정렬하고 문자열로 합치기
    answer = "".join(sorted(unique_chars))
    return answer