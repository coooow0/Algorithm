import sys
input = sys.stdin.readline

# 확장자 별로 정리해서 몇개씩 있는지 ㅇㅇ
# 보기 편하게 사전 순으로 정렬

n = int(input())

arr = dict()

for _ in range(n):
    f = list(input().strip().split('.'))
    if f[1] in arr:
        arr[f[1]] += 1
    else:
        arr[f[1]] = 1

arr_key = list(arr.keys())
arr_key.sort()

for i in arr_key:
    print(i, arr[i])
    