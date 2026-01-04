n = int(input())
arr = list(map(int, input().split()))

res = 1

# arr[0]이 arr[1]보다 클 때만 같이 넘어짐. 같으면 안 넘어지는겅미 

for i in range(1, n):
    if arr[i - 1] <= arr[i]:
        res += 1
print(res)