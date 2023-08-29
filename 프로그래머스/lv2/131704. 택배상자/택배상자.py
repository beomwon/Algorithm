def solution(order):
    answer, st, cur = 0, [], 0

    for i in range(1, len(order) + 1):
        st.append(i)
        while st and st[-1] == order[cur]:
            st.pop()
            cur += 1
            answer += 1

    return answer