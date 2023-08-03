def solution(arr1, arr2):
    la, lb = len(arr1), len(arr2)
    sa, sb = sum(arr1), sum(arr2)
    if la > lb or (la==lb and sa > sb): return 1
    if lb > la or (la==lb and sb > sa): return -1
    return 0