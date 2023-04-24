def solution(a, b, c, d):
    sets = sorted([[k, [a,b,c,d].count(k)] for k in set([a,b,c,d])], key=lambda x:-x[1])
    
    if sets[0][1] == 4: return 1111*sets[0][0]
    elif sets[0][1] == 3: return (10*sets[0][0] + sets[1][0])**2
    elif sets[0][1] == 2 and sets[1][1] == 2: return (sets[0][0]+sets[1][0])*((sets[0][0]-sets[1][0])**2)**0.5
    elif sets[0][1] == 2 and sets[1][1] == 1: return sets[1][0]*sets[2][0]
    else: return min([a,b,c,d])