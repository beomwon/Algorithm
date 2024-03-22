def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    alpha = lottos.count(0)
    basic = sum(lottos.count(v) for v in win_nums)
    return [rank[alpha+basic], rank[basic]]