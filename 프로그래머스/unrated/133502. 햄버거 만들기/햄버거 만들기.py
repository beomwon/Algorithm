def solution(ingredient):
    answer = 0
    stack = []

    for i in range(len(ingredient)):
        stack.append(ingredient[i])
        ham = ""
        if len(stack) >= 4:
            ham += str(stack[-1]) + str(stack[-2]) + str(stack[-3]) + str(stack[-4])
            if ham == "1321":
                answer += 1
                for j in range(4):
                    stack.pop()


    return answer