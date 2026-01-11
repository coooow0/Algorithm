import sys
input = sys.stdin.readline

line = list(map(str, input().strip()))

t = int(input().strip())

stack = []

for _ in range(t):
    arr = list(map(str, input().strip().split()))
    
    if line and arr[0] == 'L':
        # line에 원소가 있는데 L을 한거면
        stack.append(line.pop())
        
    elif stack and arr[0] == 'D':
        # stack에 원소가 있으면
        line.append(stack.pop())
        
    elif line and arr[0] == 'B':
        del line[-1]
    
    elif arr[0] == 'P':
        line.append(arr[1])

print(''.join(line + stack[::-1]))