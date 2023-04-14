def solution(s):
    for i, v in enumerate(['zero','one','two','three','four','five','six','seven','eight','nine']):
        s = s.replace(v,str(i))
    return int(s)
