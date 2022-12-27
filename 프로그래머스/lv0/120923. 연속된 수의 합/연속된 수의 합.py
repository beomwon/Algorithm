import math
def solution(num, total):
    start = int(total/num) - (math.ceil(num/2) - 1)
    return [x for x in range(start, num+start)]