def solution(arr, delete_list):
    for v in delete_list:
        if v in arr:
            arr.remove(v)
    return arr