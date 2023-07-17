def solution(n,a,b):
    answer, a, b = 0, a-1, b-1
    
    while (a:=a//2) != (b:=b//2):
        answer += 1
    
    return answer+1