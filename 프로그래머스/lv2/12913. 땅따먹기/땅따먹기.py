def solution(l):
    for y in range(1,len(l)):
        for x in range(4):
            # v = l[y-1].copy()
            # v.remove(l[y-1][x])
            # l[y][x] += max(v)
            # print(l[y][:l[y].index(l[y][x])]+l[y][l[y].index(l[y][x])+1:])
            l[y][x] += max(l[y-1][:l[y-1].index(l[y-1][x])]+l[y-1][l[y-1].index(l[y-1][x])+1:])
            
    return max(l[-1])