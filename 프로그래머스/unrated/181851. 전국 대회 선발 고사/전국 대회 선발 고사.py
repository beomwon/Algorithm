def solution(rank, attendance):
    r = sorted([r for r,a in zip(rank,attendance) if a])[:3]
    return 10000*rank.index(r[0]) + 100*rank.index(r[1]) + rank.index(r[2])