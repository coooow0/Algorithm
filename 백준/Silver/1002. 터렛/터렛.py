import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().strip().split())
    
    d = (x1 - x2) ** 2 + (y1 - y2) ** 2
    sum_r = (r1 + r2) ** 2
    diff_r = (r1 - r2) ** 2
    if d == 0:
        if r1 == r2:
            # 위치의 개수가 무한대임
            print(-1)
        else:
            print(0)
    else:
        # 다르면 점 두개인지 하나인지 체크하면 됨
        if sum_r == d or diff_r == d:
            print(1)
        elif diff_r < d < sum_r:
            print(2)
        else:
            print(0)