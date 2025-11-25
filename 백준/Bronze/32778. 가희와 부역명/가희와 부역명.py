import sys
input = sys.stdin.readline

line = input().strip()

if line[-1] == ')':
    line = list(map(str, line.split()))
    print(line[0])
    
    for i in range(1, len(line)):
        print(line[i].replace('(', '').replace(')', ''), end=' ')
    
else:
    print(line)
    print('-')