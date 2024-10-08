def ms(time):
    m, s = map(int, time.split(':'))
    return m*60 + s

def solution(vl, pos, op_start, op_end, commands):
    vl, pos, op_start, op_end = ms(vl), ms(pos), ms(op_start), ms(op_end)
    cal = {'next': 10, 'prev': -10}
    
    for command in commands:
        if op_start <= pos and pos <= op_end: pos = op_end
        pos = max(min(vl, pos + cal[command]), 0)
    
    if op_start <= pos and pos <= op_end: pos = op_end    
    m, s = divmod(pos, 60)
    answer = str(m).zfill(2) + ":" + str(s).zfill(2)
    return answer