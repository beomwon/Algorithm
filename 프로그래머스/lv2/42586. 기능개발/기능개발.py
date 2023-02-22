import numpy as np

def solution(p, s):
    res=[]
    
    while len(p):
        print(p)
        for i in range(len(p)):
            p[i] += s[i]
        
        remove_item = []
        for v in p:
            if v >= 100:
                remove_item.append(v)
            else:
                break
                
        if len(remove_item) > 0:   
            res.append(len(remove_item))
            
            for v in remove_item:
                p.remove(v)
                s.pop(0)
        
    return res