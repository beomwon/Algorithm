def solution(bandage, health, attacks):
    count = 0
    max_health = health
    for time in range(attacks[-1][0]+1):
        if time == attacks[0][0]:
            _, damage = attacks.pop(0)
            health -= damage
            count = 0
            if health <= 0:
                return -1
        else:
            count += 1
            if count%bandage[0] == 0:
                count = 0
                health += bandage[2]
            health += bandage[1]
            health = min(max_health, health)
            
    return health