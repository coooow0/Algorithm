n = int(input())
arr=[[0] * 3] * n

for i in range(n):
    arr[i] = list(map(int, input().split()))

for i in range(1, n):
    arr[i][0] = min(arr[i-1][1], arr[i-1][2]) + arr[i][0]
    arr[i][1] = min(arr[i-1][0], arr[i-1][2]) + arr[i][1]
    arr[i][2] = min(arr[i-1][1], arr[i-1][0]) + arr[i][2]
print(min(arr[n-1][0], arr[n-1][1], arr[n-1][2]))