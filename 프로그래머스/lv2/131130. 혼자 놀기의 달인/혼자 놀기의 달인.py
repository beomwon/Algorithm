def solution(cards):
    boxs, cur, index, count = [], 0, 0, 0
    
    while index < len(cards):
        if cards[index] == -1:
            index += 1

        if cards[cur] == -1:
            cur = index
            boxs.append(count)
            count = 0
        else:
            temp = cards[cur]
            cards[cur] = -1
            cur = temp - 1
            count += 1
            
    boxs.sort()
    return boxs[-1]*boxs[-2]