import sys
input = sys.stdin.readline

p = 'I'
ps = 'OI'

n = int(input().strip())
m = int(input().strip())

p = p + ps * n

arr = list(input().strip())

cnt = 0

for i in range(m-len(p) + 1):
    line = ''
    for k in arr[i:i+len(p)]:
        line += k
        
    if line == p:
        cnt += 1
    
print(cnt)