import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
# arr의 i번째에서 j 번째까지 수의 합이 m이 되는 경우의 수

cnt = 0

for i in range(n):
    s = 0
    for k in range(i, n):
        s += arr[k]
        if s == m:
            cnt += 1
        elif s > m:
            break
            
print(cnt)