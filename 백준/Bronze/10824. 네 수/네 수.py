import sys
input = sys.stdin.readline

a, b, c, d = map(str, input().split())
print(int(a+b) + int(c+d))