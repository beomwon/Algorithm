def solution(cards1, cards2, goal):
    i1=0
    i2=0
    for v in goal:
        
        if i1 < len(cards1) and v == cards1[i1]:
            i1 += 1
        elif i2 < len(cards2) and v == cards2[i2]:
            i2 += 1
        else:
            return 'No'
    return 'Yes'