import sys
input = sys.stdin.readline

arr = list(input().strip())

## 현 연산자보다 스택 맨 위의 값이 작은 경우, 멈추고
# 스택 맨 위의 값보다 크거나 같은 경우 계속 팝

stack = []

for i in arr:
    if i == '(':
        stack.append(i)
        
    elif i == ')':
        while True:
            if stack[-1] == '(':
                stack.pop()
                break
            print(stack.pop(), end='')
    elif i in ['*', '/']: # 우선 순위가 높은 연산자의 경우
        if len(stack) == 0 or stack[-1] in ['(', '-', '+']:
            # 비어있거나, 낮은 연산자면 그냥 넣음
            stack.append(i)
        else: # 같거나 큰 연산자의 경우
            while stack and stack[-1] != '(': # 스택이 안 비어있고, 스택의 탑이 여는 괄호가 아니면 진행
                if stack[-1] in ['+', '-']:
                    # 낮은 연산자가 나오면 멈춤
                    break
                else: # 같은 연산자면 pop
                    print(stack.pop(), end='')
            stack.append(i)
            
    elif i in ['-', '+']:
        if len(stack) == 0 or stack[-1] == '(':
            # 비어있거나, 여는 괄호면 넣음
            stack.append(i)
        else:
            while stack and stack[-1] != '(':
                print(stack.pop(), end='')
            stack.append(i)
    else:
        print(i, end='')

if len(stack) != 0:
    while stack:
        print(stack.pop(), end='')