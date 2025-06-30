# 점수를 최대로
# 교실 점수의 합이 최대가 되도록 << !!

n, k = map(int, input().split())
arr = list(map(int, input().split()))

# 누적합
for i in range(1, n):
    arr[i] += arr[i - 1]
    
arr.sort()
print(sum(arr[-k:]))