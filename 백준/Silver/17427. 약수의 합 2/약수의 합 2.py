import sys
input = sys.stdin.readline

n = int(input())

num = 0

for i in range(1, n + 1):
    num += (n // i) * i
print(num)