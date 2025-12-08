import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    line = input().strip()
    line = line.upper()
    n = len(line)

    res = True
    
    for i in range(n // 2):
        if line[i] != line[n - i - 1]:
            res = False
            break
            
    print('Yes' if res else 'No')