def solution(length, threshold, trucks):
    answer = 0
    bridge = [0]*length
    cur_weight = 0
    trucks = trucks[::-1]
    while trucks:
        answer += 1
        cur_weight -= bridge.pop(0)
        if cur_weight + trucks[-1] <= threshold:
            w = trucks.pop()
            cur_weight += w
            bridge.append(w)
        else:
            bridge.append(0)
        
    return answer + len(bridge)