import math

def solution(fees, records):
    calculates = {}
    for record in records:
        time, vnum, info = record.split()
        hour, minute = map(int, time.split(':'))
        
        if vnum in calculates.keys():
            if info == 'IN':
                calculates[vnum][1:] = [hour*60 + minute, 1439]
            else:
                calculates[vnum][0] += ((hour*60 + minute) - calculates[vnum][1])
                calculates[vnum][1:] = [0, 0]
        else:
            calculates[vnum] = [0, hour*60 + minute, 1439]
        
    result = []
    for vnum, fare in calculates.items():
        total = fare[0] + (fare[2] - fare[1])
        extra = math.ceil((total-fees[0])/fees[2])*fees[3]
        fee = fees[1] + (extra if extra > 0 else 0)
        result.append([vnum, fee])
    
    return [v[1] for v in sorted(result, key=lambda x: x[0])]