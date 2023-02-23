def solution(operations):
    answer = []
    for op in operations:
        func, value = op.split()
        if func == 'I':
            answer.append(int(value))
        elif len(answer) > 0:
            if value == '-1':
                answer.pop(answer.index(min(answer)))
            else:
                answer.pop(answer.index(max(answer)))
                
    if len(answer) == 0:
        return [0, 0]
    
    return [max(answer), min(answer)]