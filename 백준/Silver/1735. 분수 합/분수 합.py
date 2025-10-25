import sys
input = sys.stdin.readline

n, m = map(int, input().split())
x, y = map(int, input().split())

son = n * y + x * m
mom = m * y
# a는 분자, b는 분모

small = son
tmp = mom

while tmp != 0:
    small, tmp = tmp, small%tmp

print(son // small, mom // small)