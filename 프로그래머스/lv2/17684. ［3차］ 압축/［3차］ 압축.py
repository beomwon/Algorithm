
def solution(msg):
    dic, answer, i, s = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], [], 0, msg[0]

    while i != len(msg):
        if s in dic:
            if i != len(msg)-1:
                i += 1
            else:
                answer.append(dic.index(s)+1)
                break
            s += msg[i]
        else:
            dic.append(s)
            answer.append(dic.index(s[:-1])+1)
            s = msg[i]
    return answer