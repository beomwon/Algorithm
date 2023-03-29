def solution(word):
    answer = 0
    dic={'A':0,'E':1,'I':2,'O':3,'U':4}
    for i in range(len(word)):
        answer+=1+dic[word[i]]*((5**(5-i)-1)/4)

    return answer