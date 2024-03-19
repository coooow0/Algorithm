import sys

input = sys.stdin.readline
n, m = map(int, input().split())

N_arr =[]; M_arr=[]; dic = {}; arr = []
for i in range(n):
    N_arr.append(input().strip())
for i in range(m):
    M_arr.append(input().strip())

for i in N_arr:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

cnt = 0

for i in M_arr:
    if i in dic:
        arr.append(i)
        cnt += 1

arr.sort()

print(cnt)
for i in arr:
    print(i)
# dic = {} # 사전형으로 찾기 
# 만약 a['algo'] = 'rithm' 이면, print(a['algo'])시 rithm 이 출력됨
