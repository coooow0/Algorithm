n, m = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
res = 0 # 최종 출력하는 겂
start = 0

ans_sum = 0
for end in range(n):
    ans_sum += arr[end]
    
    while ans_sum > m:
        ans_sum -= arr[start]
        start += 1
    
    if ans_sum == m:
        res += 1
    
print(res)
    