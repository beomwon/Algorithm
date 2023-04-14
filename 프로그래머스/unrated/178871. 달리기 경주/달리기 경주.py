def solution(players, callings):
    rd = {k+1:v for k, v in enumerate(players)}
    pd = {k:v+1 for v, k in enumerate(players)}

    for cp in callings:
        cr=pd[cp]
        pp=rd[cr-1]
        
        rd[cr-1],rd[cr]=rd[cr],rd[cr-1]
        pd[pp],pd[cp]=pd[cp],pd[pp]
        
    return list(rd.values())