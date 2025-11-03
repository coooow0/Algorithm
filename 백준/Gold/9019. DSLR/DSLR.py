import sys
from collections import deque

t = int(input().strip())

for _ in range(t):
    a, b = map(int, input().strip().split())
    
    visited = [None for _ in range(10000)]
    
    queue = deque()
    
    queue.append(a) # 시작 번호를 큐에 넣음
    visited[a] = ''
    
    while queue:
        q = queue.popleft()
        # 첫 값을 넣음
        
        if q == b: # 찾는 값이면 반환하고 멈춤
            print(visited[q])
            break
        
        # D
        d = q * 2 % 10000
        if visited[d] is None:
            visited[d] = visited[q] + 'D'
            queue.append(d)
        
        # S
        s = (q - 1) % 10000
        if visited[s] is None:
            visited[s] = visited[q] + 'S'
            queue.append(s)
            
        # L
        l = (q % 1000) * 10 + (q // 1000)
        if visited[l] is None:
            visited[l] = visited[q] + 'L'
            queue.append(l)
            
        # R
        r = (q % 10) * 1000 + (q // 10)
        if visited[r] is None:
            visited[r] = visited[q] + 'R'
            queue.append(r)
            
    