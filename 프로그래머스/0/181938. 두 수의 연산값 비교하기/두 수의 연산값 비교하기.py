def solution(a, b):
    sum_str = int(str(a) + str(b))
    mul_str = 2 * a * b 
    if sum_str >= mul_str:
        return sum_str
    else:
        return mul_str