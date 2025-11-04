import sys
input = sys.stdin.readline

n = int(input().strip()) # IOI
m = int(input().strip()) # 문자열 길이

i = 'I'
oi = 'OI' * n
line = i + oi

arr = input().strip()

i = 0

cnt = 0
ans = 0

while i <= m - 3:
    if arr[i:i+3] == 'IOI':
        cnt += 1
        i += 2
        if cnt == n:
            ans += 1
            cnt -= 1
            
    else:
        i += 1
        cnt = 0
print(ans)