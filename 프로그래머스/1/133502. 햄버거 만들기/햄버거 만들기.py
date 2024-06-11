def solution(ingredient):
    # ingredient = 재료 정보
    answer = 0
    stack = []
    for i in ingredient:
        stack.append(i)
        if len(stack) >= 4 and stack[-4:] == [1, 2, 3, 1]:
            answer += 1
            for j in range(4):
                stack.pop()
    return answer