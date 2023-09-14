def solution(plans):
    plans = [[n, int(s.split(':')[0])*60 + int(s.split(':')[1]),int(p)] for n, s, p in plans]
    plans = sorted(plans, key=lambda x:-x[1])
    stack, answer = [plans.pop()], []
    time = stack[-1][1]
    
    while plans:
        if stack:
            stack[-1][2] -= 1
            if stack[-1][2] == 0:
                answer.append(stack.pop()[0])
                
        if plans[-1][1] == time:
            stack.append(plans.pop())
            
        time += 1
    
    while stack:
        answer.append(stack.pop()[0])
                   
    return answer
