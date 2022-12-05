def solution(number, limit, power):
    k = [1 for _ in range(number+1)]
    c = [0 for _ in range(number+1)]
    for i in range(len(k)):
        if i == 0:
            continue
        for j in range(i,len(k),i):
            k[j] *= i
            c[j] += 1
    c = c[1:]
    answer = 0
    for i in c:
        if i <= limit:
            answer += i
        else:
            answer += power

    return answer