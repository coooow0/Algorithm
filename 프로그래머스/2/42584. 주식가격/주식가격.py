def solution(prices):
    answer = [0 for _ in range(len(prices))]
    stack = []
    
    for i in range(len(prices)):
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            answer[j] = i - j
    
        stack.append(i) # 인덱스를 넣기
    
    # print(answer, stack)
    
    while stack:
        j = stack.pop()
        answer[j] = len(prices) - j - 1
        
    
    return answer