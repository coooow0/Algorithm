import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())

arr = list(map(int, input().strip().split()))

sum_arr = [0]

for i in range(n):
    sum_arr.append(arr[i] + sum_arr[i])
    
    
for _ in range(m):
    a, b = map(int, input().strip().split())
    
    print(sum_arr[b] - sum_arr[a - 1])