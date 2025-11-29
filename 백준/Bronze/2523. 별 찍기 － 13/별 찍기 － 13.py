import sys
input = sys.stdin.readline

n = int(input().strip())

for i in range(1, n + 1):
    print('*' * i)

for i in range(n - 1, 0, -1):
    print('*' * i)