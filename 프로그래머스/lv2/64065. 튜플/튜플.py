def solution(s):
    answer = []
    for _list in sorted(eval(s.replace('{','[').replace('}',']')), key=lambda x: len(x)):
        for v in _list:
            if v not in answer:
                answer.append(v)
                break
                
    return answer