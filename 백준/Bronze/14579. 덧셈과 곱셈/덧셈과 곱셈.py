import sys
input = sys.stdin.readline

a, b = map(int, input().strip().split())
cnt = 1

for i in range(a, b + 1):
    num = 0
    for k in range(1, i + 1):
        num += k
    cnt *= num
print(cnt % 14579)