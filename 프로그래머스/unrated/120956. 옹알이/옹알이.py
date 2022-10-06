def solution(babbling):
    babbling_list = {'a':'aya', 'y':'ye', 'w':'woo', 'm':'ma'}

    answer = 0
    for word in babbling:                   # 검증할 문장
        stack = list()
        flag = True
        keys = babbling_list.keys()

        while word and word[0] in keys:
            if len(word) < 2:
                break
            new_stack = word[0]
            word = word.replace(babbling_list[word[0]],'',1)
            if not stack or stack[-1] != new_stack:
                stack.append(new_stack)
            elif stack[-1] == new_stack:
                flag = False
                break

        if not word and flag:
            answer +=1

    return answer