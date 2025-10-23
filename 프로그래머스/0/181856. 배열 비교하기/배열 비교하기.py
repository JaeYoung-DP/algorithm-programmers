def solution(arr1, arr2):
    if len(arr1) < len(arr2):
        return -1
    elif len(arr1) > len(arr2):
        return 1
    
    sum_arr1 = sum(arr1)
    sum_arr2 = sum(arr2)
    if sum_arr1 < sum_arr2:
        return -1
    elif sum_arr1 > sum_arr2:
        return 1
    
    # 길이와 합이 같으면 두 배열은 같다.
    return 0