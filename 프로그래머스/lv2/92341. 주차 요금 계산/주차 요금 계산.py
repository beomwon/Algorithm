import math
def solution(fees, records):
    sales = {}
    for record in records:
        time, vnum, info = record.split()
        hour, minute = map(int, time.split(':'))
        
        if vnum in sales:
            if info == 'IN':
                sales[vnum][1:] = [hour*60 + minute, 1439]
            else:
                sales[vnum][0] += ((hour*60 + minute) - sales[vnum][1])
                sales[vnum][1:] = [0, 0]
        else:
            sales[vnum] = [0, hour*60 + minute, 1439]
        
        
    result = []
    for vnum, fare in sales.items():
        total = fare[0] + (fare[2] - fare[1])
        extra = math.ceil((total-fees[0])/fees[2])*fees[3]
        fee = fees[1] + (extra if extra > 0 else 0)
        result.append([vnum, fee])
    
    return [v[1] for v in sorted(result, key=lambda x: x[0])]