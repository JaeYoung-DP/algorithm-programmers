def solution(arr):
    stk = []
    for i in range(len(arr)):
        if stk==[]:
            stk += [arr[i]]
        elif stk:
            if stk[-1]==arr[i]:
                del stk[-1]
            else:
                stk += [arr[i]]
    if stk==[]:
        stk=[-1]
    return stk