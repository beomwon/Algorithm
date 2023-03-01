import re
def solution(skill, skill_trees):
    answer = 0
    for s in skill_trees:
        able = True
        for i, step in enumerate(re.findall(f'[{skill}]', s)):
               if skill[i] != step:
                    able = False
        answer += int(able)
    return answer