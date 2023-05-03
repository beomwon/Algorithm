def solution(l):
    for c, v in enumerate(l):
        if v == 'l': return l[:c]
        if v == 'r': return l[c+1:]
    return []