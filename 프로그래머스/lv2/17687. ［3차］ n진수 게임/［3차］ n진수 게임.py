def convert(num, base) :
    q, r = divmod(num, base)
    return (convert(q, base) if q else '') + '0123456789ABCDEF'[r]
    
def solution(n, t, m, p):
    game, target = '', -1
    while len(game) <= m*(t+1):
        game += convert(target:=target+1, n)
        
    return game[p-1::m][:t]