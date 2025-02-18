n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))


cnt = 0
res = 0
start = 0
for end in range(n):
    res += arr[end]
    
    while res > m: # res가 m을 초과하면 start부분에 있는 원소를 차례대로 제거함
        res -= arr[start]
        start += 1
    
    if res == m:
        cnt += 1
print(cnt)