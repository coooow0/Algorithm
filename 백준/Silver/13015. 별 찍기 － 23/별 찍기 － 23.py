import sys
input = sys.stdin.readline

n = int(input().strip())

for i in range(n):
    if i == 0:
        print('*' * n + (' ' * (2 * (n - 2 - i) + 1)) + '*' * n)
    elif i < n - 1:
        print(' ' * i + '*' + ' ' * (n - 2) + '*' +  (' ' * (2 * (n - 2 - i) + 1))  + '*' + ' ' * (n - 2) + '*') 
    else:
        print(' ' * i + '*' +' ' * (n - 2) + '*' + ' ' *(n - 2) + '*')
    
for i in range(n - 2, -1, -1):
    if i == 0:
        print('*' * n + (' ' * (2 * (n - 2 - i) + 1)) + '*' * n)
    else:
        print(' ' * i + '*' + ' ' * (n - 2) + '*' +  (' ' * (2 * (n - 2 - i) + 1))  + '*' + ' ' * (n - 2) + '*') 