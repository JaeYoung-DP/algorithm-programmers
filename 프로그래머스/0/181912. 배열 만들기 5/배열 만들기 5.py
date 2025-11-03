def solution(intStrs, k, s, l):
    answer = []
    for a in intStrs:
        a_list=list(a)[s:s+l]
        if int("".join(a_list)) > k:
            answer.append(int("".join(a_list)))
    return answer