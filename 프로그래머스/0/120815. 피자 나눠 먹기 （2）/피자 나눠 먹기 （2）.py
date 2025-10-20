import math
def lcm(n, m):
    return n // math.gcd(n, m) * m

def solution(n):
    answer = lcm(n, 6) // 6
    return answer