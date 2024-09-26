# 국영수
import sys
input = sys.stdin.readline

n = int(input())

arr = [['', 0,0,0] for _ in range(n)]
for i in range(n):
    arr[i] = input().split()
    arr[i][1], arr[i][2], arr[i][3] = int(arr[i][1]), int(arr[i][2]), int(arr[i][3])

arr.sort(key=lambda x : (-x[1], x[2], -x[3], x[0]))
# 람다식에서 앞에 -가 붙은 것은 내림차순 정렬. 기본으로는 오름차순이다. 
for i in range(n):
    print(arr[i][0])