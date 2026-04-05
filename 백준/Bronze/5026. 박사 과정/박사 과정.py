import sys
input = sys.stdin.readline

n = int(input().strip())

for _ in range(n):
    line = input().strip().split('+')
    
    if len(line) == 1:
        print('skipped')
    else:
        print(int(line[0]) + int(line[1]))
    