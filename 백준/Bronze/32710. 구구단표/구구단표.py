import sys
input = sys.stdin.readline

n = int(input())

for i in range(2, 10):
    for k in range(1, 10):
        if i == n or k == n or i*k == n:
            print(1)
            exit()
print(0)