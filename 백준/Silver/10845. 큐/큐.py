# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 큐에 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
import sys
from collections import deque
n = int(sys.stdin.readline().strip())
queue = []
queue = deque()
for i in range(n):
    inner = sys.stdin.readline().strip().split()
    if inner[0] == 'push':
        queue.append(inner[1])
    else:
        if inner[0] == 'pop':
            if queue: #비어있지 않으면
                print(queue[0])
                queue.popleft() #popleft = 맨 앞에 수를 pop함. pop()은 맨 뒤에 수.
            else:
                print(-1)

        elif inner[0] == 'size':
            print(len(queue))
        
        elif inner[0] == 'empty':
            if queue:
                print(0)
            else:
                print(1)
        
        elif inner[0] == 'front':
            if queue:
                print(queue[0])
            else:
                print(-1)

        else:
            if queue:
                print(queue[-1])
            else:
                print(-1)
                

