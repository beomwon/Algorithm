def solution(s):
    answer = []
    dic = {}
    for i in range(len(s)):
        if s[i] in dic.keys():
            answer.append(i-dic[s[i]])
            dic[s[i]] = i
        else:
            answer.append(-1)
            dic[s[i]] = i
    return answer