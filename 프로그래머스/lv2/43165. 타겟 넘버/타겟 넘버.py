temp = []

def recur(n, i, cur):
    if i == len(n):
        temp.append(cur)
    else:
        recur(n, i+1, n[i]+cur)
        recur(n, i+1, -n[i]+cur)
        
def solution(n, t):
    recur(n, 0, 0)
    return temp.count(t)