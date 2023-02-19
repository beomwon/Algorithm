def solution(dartResult):
    dartResult = list(dartResult + 'E')
    answer = [0]
    num = ''
    for i, v in enumerate(dartResult):
        if '0'<= v <= '9':
            num += v
        elif v in ['S','D','T']:
            num = int(num)**(['S','D','T'].index(v)+1)
            if dartResult[i+1] == '*':
                answer[-1] *= 2
                answer.append(num*2)
            elif dartResult[i+1] == '#':
                answer.append(-num)
            else:
                answer.append(num) 
            num = ''
    print(answer)
    return sum(answer)