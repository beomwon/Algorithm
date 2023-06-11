def solution(arr, queries):
    answer = []
    for s,e,i in queries:
        flag = True
        for v in sorted(arr[s:e+1]):
            if v > i:
                answer.append(v)
                flag = False
                break
        if flag:
            answer.append(-1)
    return answer