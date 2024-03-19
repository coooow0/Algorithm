import sys

input = sys.stdin.readline

n = int(input())
n_arr =list(map(int, input().split()))

m = int(input())
m_arr = list(map(int, input().split()))

dic = {}
for i in m_arr:
    dic[i] = 0

for i in n_arr:
    if i in dic:
        dic[i] = 1

for i in dic:
    print(dic[i], end=' ')
    