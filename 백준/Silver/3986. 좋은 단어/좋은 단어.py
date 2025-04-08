# 좋은 단어
n = int(input())
cnt = 0

for _ in range(n):
    arr = list(input())
    stack = []
    
    for i in arr:
        if len(stack) == 0:
            stack.append(i)
        elif i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)
    
    if len(stack) == 0:
        cnt += 1
print(cnt)
        