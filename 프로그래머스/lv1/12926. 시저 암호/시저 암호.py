from collections import deque

def solution(s, n):
    big = deque([chr(i) for i in range(ord('A'), ord('Z')+1)])
    small = deque([chr(i) for i in range(ord('a'), ord('z')+1)])
    answer = ''
    big.rotate(-n)
    small.rotate(-n)
    for w in s:
        if 'a' <= w <= 'z':
            answer += small[ord(w)-ord('a')]
        elif 'A' <= w <= 'Z':
            answer += big[ord(w)-ord('A')]
        else:
            answer += w
    
    return answer