def solution(s):
    ans, pair = 0, {'{':'}', '[':']', '(':')'}
    for i in range(len(s)):
        iscorrect, stack = True, []
        for v in s:
            if v in ['{','[','(']: stack.append(v)
            else:
                if not stack:
                    iscorrect = False
                    break
                else:
                    if v != pair[stack[-1]]:
                        iscorrect = False
                        break
                    else:
                        stack = stack[:-1]
                        
        if iscorrect and not stack:
            ans += 1
        
        s = s[1:]+s[0]
    return ans