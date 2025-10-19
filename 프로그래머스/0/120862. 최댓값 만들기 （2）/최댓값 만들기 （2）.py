def solution(numbers):
    numbers.sort() # 배열을 오름차순으로 정렬
    max_product = numbers[-1] * numbers[-2] # 가장 큰 두 수의 곱
    min_product = numbers[0] * numbers[1]   # 가장 작은 두 수의 곱
    return max(max_product, min_product)