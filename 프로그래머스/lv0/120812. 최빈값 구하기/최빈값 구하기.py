def solution(array):
    max_value = [-1, -1, 0]
    
    for v in set(array):
        v_count = array.count(v)

        if  v_count > max_value[1]:
            max_value = [v, array.count(v), 0]
        elif v_count == max_value[1]: 
            max_value[-1] = 1
    
    return -1 if max_value[-1] else max_value[0]
        