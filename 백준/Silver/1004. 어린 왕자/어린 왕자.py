import sys
input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    sx, sy, ex, ey = map(int, input().strip().split())
    # start x, start y, end x, end y 라는 뜻
    n = int(input().strip())
    cnt = 0
    
    for _ in range(n):
        cx, cy, r = map(int, input().strip().split())
        
        start_dot = (sx - cx) ** 2 + (sy - cy) ** 2
        end_dot = (ex - cx) ** 2 + (ey - cy) ** 2
    
        
        if start_dot < r ** 2 and end_dot > r ** 2:
            cnt += 1
        elif end_dot < r ** 2 and start_dot > r ** 2:
            cnt += 1
        
    print(cnt)

    