def solution(polynomial):
    x, n = 0, 0
    for v in polynomial.replace(' ','').split('+'):
        if 'x' == v: x += 1
        elif 'x' in v: x += int(v[:-1])
        else: n += int(v)
    if x == 0:
        return str(n)
    if n == 0:
        return str(x)+'x' if x > 1 else 'x'
    if x == 0 and n == 0:
        return '0'
    return f'{x}x + {n}' if x > 1 else f'x + {n}'