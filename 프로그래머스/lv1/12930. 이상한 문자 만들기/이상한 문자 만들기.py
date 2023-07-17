def solution(s):
    i = 0
    ans = ''
    for w in s:
        if w == ' ':
            i = 0
            ans += w
        else:
            if i%2 == 0:
                ans += w.upper()
            else:
                ans += w.lower()
            i += 1
    return ans
            
















# def solution(s):
#     answer = ''
#     flag = True
#     for i in range(len(s)):
#         if s[i] == ' ':
#             answer+= s[i]
#             flag = False
#         else:
#             if flag:
#                 answer+= s[i].upper()
#             else:
#                 answer+= s[i].lower()
#         flag = not flag
        
#     return answer