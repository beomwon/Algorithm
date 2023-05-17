def solution(data, col, row_begin, row_end):
    answer = 0
    for i, d in enumerate(sorted(data, key=lambda x: (x[col-1],-x[0]))[row_begin-1:row_end]):
        answer ^= sum([n%(i+row_begin) for n in d])
    
    return answer