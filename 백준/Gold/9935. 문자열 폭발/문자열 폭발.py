import sys
input = sys.stdin.readline

arr = input().strip()
bomb = input().strip()

stack = []
for i in range(len(arr)):
    stack.append(arr[i])

    if stack[-1] == bomb[-1]:
        string = ''
        if len(stack) >= len(bomb):
            for i in range(len(bomb), 0, -1):
                string += stack[-i]
                
            if string == bomb:
                for _ in range(len(bomb)):
                    stack.pop()
        
    
if stack:
    for i in stack:
        print(i, end='')
else:
    print("FRULA")