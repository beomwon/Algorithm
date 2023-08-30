def solution(routes):
    order = []
    for i, (s, e) in enumerate(routes):
        order += [[s, 0, i], [e, 1, i]]
    
    answer, pass_car, check = 0, [], []
    for _, out, index in sorted(order):
        if out:
            if index not in check:
                answer += 1
                check += pass_car
                pass_car = []
        else:
            pass_car.append(index)
            
    return answer