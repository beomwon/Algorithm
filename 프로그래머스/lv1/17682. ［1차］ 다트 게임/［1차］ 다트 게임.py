def solution(r):
    stack, i, num = [], 0, 0
    square = {'S':1, 'D':2, 'T':3}
    while i < len(r):
        if '0'<= r[i] <= '9':
            if r[i] == '1' and r[i+1] == '0':
                num = 10
                i+=1
            else:
                num = int(r[i])
            stack.append(num)
        
        elif r[i] in ['S', 'D', 'T']:
            stack[-1] = stack[-1]**square[r[i]]
        
        elif r[i] == '*':
            stack[-1] = stack[-1]*2
            if len(stack) != 1:
                stack[-2] = stack[-2]*2
            
        elif r[i] == '#':
            stack[-1] = -stack[-1]
        
        i += 1
        
    return sum(stack)












# def solution(dartResult):
#     dartResult = list(dartResult + 'E')
#     answer = [0]
#     num = ''
#     for i, v in enumerate(dartResult):
#         if '0'<= v <= '9':
#             num += v
#         elif v in ['S','D','T']:
#             num = int(num)**(['S','D','T'].index(v)+1)
#             if dartResult[i+1] == '*':
#                 answer[-1] *= 2
#                 answer.append(num*2)
#             elif dartResult[i+1] == '#':
#                 answer.append(-num)
#             else:
#                 answer.append(num) 
#             num = ''
#     print(answer)
#     return sum(answer)