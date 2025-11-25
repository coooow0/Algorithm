import sys
input = sys.stdin.readline

w, h = map(int, input().strip().split())
print(w * h / 2)