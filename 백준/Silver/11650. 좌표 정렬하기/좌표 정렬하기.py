import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
arr.sort(key = lambda x : (x[0], x[1]))
for i in arr:
    print(i[0], i[1])