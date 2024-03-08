import sys
n = int(sys.stdin.readline())

for i in range(n):
    string = list(sys.stdin.readline().strip().split())
    for j in string:
        print(j[::-1], end=" ")
