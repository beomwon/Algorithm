import re
def solution(skill, skill_trees):
    answer = 0
    for s in skill_trees:
        s = ''.join(re.findall(f'[{skill}]', s))
        answer += int(s == skill[:len(s)])
    return answer