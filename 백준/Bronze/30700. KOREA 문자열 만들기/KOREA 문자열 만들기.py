import sys
input = sys.stdin.readline

stack = []

line = input().strip()
cnt = 0

for i in line:
    if len(stack) == 0 and i == 'K':
        stack.append(i)
        cnt += 1
    
    elif len(stack) == 1 and i == 'O':
        stack.append(i)
        cnt += 1
    
    elif len(stack) == 2 and i == 'R':
        stack.append(i)
        cnt += 1
        
    elif len(stack) == 3 and i == 'E':
        stack.append(i)
        cnt += 1
        
    elif len(stack) == 4 and i == 'A':
        stack.append(i)
        cnt += 1
        stack = []
        
print(cnt)