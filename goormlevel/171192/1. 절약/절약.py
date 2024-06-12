import sys
input = sys.stdin.readline
n = int(input())
result = 0
b = True
for i in range(n):
    c, v = input().split()
    
    if c == 'in':
        result += int(v)
    else:
        result -= int(v)
        
    if result < 0:
        b = False

if b == False:
    print('fail')
else:
    print('success')