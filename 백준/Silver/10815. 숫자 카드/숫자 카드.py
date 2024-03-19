import sys

input = sys.stdin.readline

n = int(input())
n_arr =set(map(int, input().split()))

m = int(input())
m_arr = list(map(int, input().split()))

for i in m_arr:
    if i in n_arr:
        print(1, end=' ')
    else:
        print(0, end=' ')