import sys
input = sys.stdin.readline

n = int(input())

y = 2024
m  = 8

if n == 1:
    print(y, m)
else:
    y = (8 + 7 * (n - 1)) // 12 + 2024
    m = (8 + 7 * (n - 1)) % 12
    if m == 0:
        y -= 1
        m = 12
        
    print(y, m)