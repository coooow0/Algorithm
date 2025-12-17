import sys
input = sys.stdin.readline

while True:
    n, m = map(int, input().split())
    
    if n == m and n == 0:
        break

    
    if n > m:
        print('Yes')
    else:
        print('No')
    