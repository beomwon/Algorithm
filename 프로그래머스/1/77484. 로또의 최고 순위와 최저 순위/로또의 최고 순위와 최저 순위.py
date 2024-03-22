def solution(lottos, win_nums):
    alpha = lottos.count(0)
    basic = 7 - sum(lottos.count(v) for v in win_nums)
    return [min(max(1, basic-alpha),6), min(6, basic)]