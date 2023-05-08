def solution(l):
    for ri in range(1,len(l)):
        for ci in range(4):
            v = l[ri-1].copy()
            v.remove(l[ri-1][ci])
            l[ri][ci] += max(v)
            
    return max(l[-1])