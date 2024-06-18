n = int(input())
temp = n
cnt = 0
while True:
    a = temp // 10
    b = temp % 10
    c = (a+b) % 10
    
    temp = b*10 + c
    cnt += 1
    if temp == n:
        break
print(cnt)