import sys
n = int(sys.stdin.readline().strip())
stack = []

for i in range(n):
    inner = sys.stdin.readline().strip().split()
    if inner[0] == 'push':
        stack.append(int(inner[1]))
    else:
        if inner[0] == 'pop':
            if stack: #비어있지 않으면
                print(stack[-1])
                stack.pop()
            else: #비어있으면
                print(-1)

        elif inner[0] == 'size':
            print(len(stack))

        elif inner[0] == 'empty':
            if stack: #비어있지 않으면 
                print(0)
            else:
                print(1)
        else: #top
            if stack:  # stack이 비어있지 않은 경우
                print(stack[-1])
            else:
                print(-1)

