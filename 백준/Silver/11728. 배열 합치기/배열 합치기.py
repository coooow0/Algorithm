import sys
input = sys.stdin.readline
n, m = map(int, input().strip().split())
# 배열 a의 크기, b의 크기가 주어짐

a = list(map(int, input().strip().split()))
a += list(map(int, input().strip().split()))
a.sort()
for i in a:
    print(i, end=' ')