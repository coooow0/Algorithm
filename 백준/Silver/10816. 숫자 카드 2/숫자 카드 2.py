import sys

input = sys.stdin.readline
n = int(input())
Narr = list(map(int, input().split()))

m = int(sys.stdin.readline())
Marr = list(map(int, input().split()))

dic = {} # 사전형으로 찾기 
# 만약 a['algo'] = 'rithm' 이면, print(a['algo'])시 rithm 이 출력됨

for i in Narr:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in Marr:
    if i in dic:
        print(dic[i], end=' ')
    else:
        print(0, end=' ')