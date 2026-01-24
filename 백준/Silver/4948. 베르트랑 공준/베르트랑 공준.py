import sys
input = sys.stdin.readline

while True:
    n = int(input().strip())
    
    if n == 0:
        break
    
    graph = [True for _ in range(2 * n + 1)]
    
    for i in range(2, int((2 * n) ** 0.5) + 1):
        if graph[i]:
            j = 2
            while i * j <= 2*n:
                graph[i*j] = False
                j += 1
    
    cnt = 0
    if n == 1:
        print(1)
        continue
    else:
        for i in range(n + 1, 2 * n + 1):
            if graph[i]:
                cnt += 1
            
    print(cnt)
    