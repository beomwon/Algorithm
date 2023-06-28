def solution(n, stations, w):
    i, answer = 0, 0
    while (i:=i+1) <= n:
        if stations and stations[0] - w <= i:
            i = stations.pop(0) + w
        else:
            i += w * 2
            answer += 1
            
    return answer