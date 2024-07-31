def solution(s):
    stack = []
    
    for i in range(len(s)):
        if len(stack) == 0:
            stack.append(s[i])
        elif stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])
    if stack:
        return 0
    else:
        return 1

    return answer