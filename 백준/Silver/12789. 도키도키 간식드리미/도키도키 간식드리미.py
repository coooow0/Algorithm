from collections import deque
import sys
input = sys.stdin.readline

n = int(input().strip())

queue = deque(list(map(int, input().strip().split())))
top = 1
stack = []

while queue:
    if queue[0] == top:
        queue.popleft()
        top += 1
        # 큐의 첫 값이랑 top이랑 같으면
        
    elif stack and stack[-1] == top:
        # 스택의 첫 값이랑 같으면 
        stack.pop()
        top += 1
        
    else: 
        # 같은 부분이 없으면 스택에 넣음
        stack.append(queue.popleft())

while stack and stack[-1] == top:
    stack.pop()
    top += 1


if len(stack) == 0 and len(queue) == 0:
    print('Nice')
else:
    print('Sad')