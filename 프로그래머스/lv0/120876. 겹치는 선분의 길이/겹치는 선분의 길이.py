def solution(lines):
    total = {}
    for line in lines:
        start, end = line
        for i in range(start*10+5, end*10, 5):
            if i in total.keys():
                total[i] = 1
            else:
                total[i] = 0
    return sum([v for k,v in total.items() if k%10!=0])