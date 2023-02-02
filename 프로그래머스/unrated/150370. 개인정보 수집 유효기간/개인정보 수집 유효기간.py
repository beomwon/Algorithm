def solution(today, terms, privacies):
    result = []
    ty, tm, td = map(int, today[2:].split('.'))
    tm += ty*12
    
    alpha_to_num = {t[0]:int(t[1:]) for t in terms}
    for i, v in enumerate(privacies):
        y, m, d = map(int, v[2:-2].split('.'))
        m += y*12 + alpha_to_num[v[-1]]
        
        print(tm, td, m, d)
        if tm < m or (tm == m and td < d): continue
            
        result.append(i+1)
    return result