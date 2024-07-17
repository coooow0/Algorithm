n = int(input())
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

arr_a.sort()

answer = 0

for i in range(n):
    answer += max(arr_b) * arr_a[i]
    arr_b.pop(arr_b.index(max(arr_b)))
print(answer)