from collections import deque

def bfs(s):
    q = deque()
    q.append(s)
    
    while q:
        x = q.popleft()
        
        if x == k:
            print(visited[x] - 1)
            return
        
        for next in [x + 1, x - 1, 2 * x]:
            if 0<= next < 1000001 and not visited[next]:
                visited[next] = visited[x] + 1
                q.append(next)


n, k = map(int, input().split())
# 경우의 수를 넣고 그 수를 visited 처리 함
visited = [0] * 1000001
visited[n] = 1
bfs(n)