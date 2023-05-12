def solution(numbers, hand):
    k, yx, res = list('123456789*0#'), {'L':[3,0], 'R':[3,2]}, ''
    for cur in numbers:
        t = [k.index(str(cur))//3, k.index(str(cur))%3]
        
        if cur in [1,4,7]: res+='L'
        elif cur in [3,6,9]: res+='R'
        else:
            ld = abs(yx['L'][0]-t[0]) + abs(yx['L'][1]-t[1])
            rd = abs(yx['R'][0]-t[0]) + abs(yx['R'][1]-t[1])
            res += 'L' if ld < rd else hand[0].upper() if ld == rd else 'R'
            
        yx[res[-1]] = t
        
    return res



# def solution(n, hand):
#     k, res = list('123456789*0#'), []
#     for v in n:
#         if v in [1,4,7]:
#             res.append('L')
#             l = [k.index(str(v))//3, k.index(str(v))%3]
#         elif v in [3,6,9]:
#             res.append('R')
#             r = [k.index(str(v))//3, k.index(str(v))%3]
#         else:
#             p = [k.index(str(v))//3, k.index(str(v))%3]
#             lv = abs(l[0]-p[0]) + abs(l[1]-p[1])
#             rv = abs(r[0]-p[0]) + abs(r[1]-p[1])
            
#             if lv == rv:
#                 if hand == 'right':
#                     r = p
#                     res.append('R')
#                 else:
#                     l = p
#                     res.append('L')
#             elif lv < rv:
#                 l = p
#                 res.append('L')
#             else:
#                 r = p
#                 res.append('R')
                
#     return ''.join(res)