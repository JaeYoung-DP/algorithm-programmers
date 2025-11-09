def solution(rank, attendance):
    Real =[]
    for i in range(len(rank)):
        if attendance[i]==True:
            Real.append(rank[i])
    Real = sorted(Real)
    a=rank.index(Real[0])
    b=rank.index(Real[1])
    c=rank.index(Real[2])
    answer = a*10000+b*100+c
    return answer