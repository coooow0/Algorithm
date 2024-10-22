n = int(input())

cnt = 0

if n == 1 or n == 3:
    print(-1)
    exit()
    
while n > 0:
    if n % 5 == 0:
        cnt += n // 5
        n = n % 5
        break
    else:
        n -= 2
        cnt += 1   
print(cnt)