def solution(want, number, discount):
    answer, wants = 0, []
    
    for v, n in zip(want, number):
        wants += [v]*n
        
    wants = sorted(wants)
    for i in range(len(discount[:-len(wants)+1])):
        answer += int(wants == sorted(discount[i:len(wants)+i]))
            
    return answer