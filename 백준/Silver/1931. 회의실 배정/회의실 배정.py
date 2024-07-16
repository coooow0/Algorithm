import sys
input = sys.stdin.readline
## 회의실의 최대 개수 = 끝나는 시간대로! 
n = int(input())
t = []
for i in range(n):
    t.append(list(map(int, input().split())))
t.sort(key=lambda x : (x[1], x[0]))
# t[a][b] b가 동일할 경우 a순으로도 정리를 해줘야함.. 
cnt = 1
arr = []
arr.append(t[0])

for i in range(1, n):
    if arr[-1][1] <= t[i][0]:
        arr.append(t[i])
        cnt += 1
print(cnt)