def solution(n, words):
    answer = [0, 0]
    
    for i in range(1, len(words)):
        if words[i-1][-1] != words[i][0]: return [i%n + 1, int(i/n) + 1]
        if words[i] in words[:i]: return [i%n + 1, int(i/n) + 1]
        
    return [0, 0]