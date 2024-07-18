import sys
input = sys.stdin.readline

n = int(input())
arr = [[0, 0] for _ in range(n)]
for i in range(n):
    arr[i][0], arr[i][1] = map(int, input().split())

# y좌표가 증가하는 순서대로. y가 같으면 x증가순으로

arr.sort(key=lambda x : (x[1], x[0]))

for i in range(n):
    print(arr[i][0], arr[i][1])