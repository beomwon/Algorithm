def solution(n, stations, w):
    i, answer = 1, 0
    while i <= n:
        if stations and stations[0] - w <= i:
            i = stations.pop(0) + w + 1
        else:
            i += w * 2 + 1
            answer += 1
            
    return answer