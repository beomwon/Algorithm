def solution(survey, choices):
    score = {k:0 for k in 'RTCFJMAN'}
    for s, c in zip(survey, choices):
        if c == 4: continue
        elif c > 4: score[s[1]] += c-4
        else: score[s[0]] += 4-c
    ans = 'R' if score['R']>=score['T'] else 'T'
    ans += 'C' if score['C']>=score['F'] else 'F'
    ans += 'J' if score['J']>=score['M'] else 'M'
    ans += 'A' if score['A']>=score['N'] else 'N'
    return ans
            