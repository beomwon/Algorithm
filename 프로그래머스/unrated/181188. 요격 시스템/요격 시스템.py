def solution(t):
    lines, overlap = 0, {'s': 0, 'e': 0}
    
    for s, e in sorted(t):
        if overlap['e'] <= s:
            lines += 1
            overlap = {'s': s, 'e': e}
        else:
            overlap = {'s': max(overlap['s'], s), 'e': min(overlap['e'], e)}
            
    return lines
