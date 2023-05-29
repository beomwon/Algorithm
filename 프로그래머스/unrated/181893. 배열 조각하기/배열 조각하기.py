def solution(arr, query):
    for i, v in enumerate(query):
        if i%2: arr = arr[v:]
        else: arr = arr[:v+1]
    return arr