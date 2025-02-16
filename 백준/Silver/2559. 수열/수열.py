import sys

input = sys.stdin.readline
n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))

new_arr = [sum(arr[:k])]

for i in range(n - k):
    new_arr.append(new_arr[i] - arr[i] + arr[k + i])
    # 구간 합. 새로운 합 = 이전 합 - 제거된 값 + 추가된 값
print(max(new_arr))
    