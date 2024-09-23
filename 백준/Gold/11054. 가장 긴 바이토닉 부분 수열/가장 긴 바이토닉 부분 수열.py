# 가장 긴 바이토닉 부분 수열
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a_reverse = a[::-1]

ins = [1] * n # 증가 수열
des = [1] * n # 감소 수열

for i in range(1, n): # 증가 수열
    for k in range(i):
        if a[i] > a[k]:
            ins[i] = max(ins[k] + 1, ins[i])
            
    for k in range(i): # 감소 수열
        if a_reverse[i] > a_reverse[k]:
            des[i] = max(des[k] + 1, des[i])
des = des[::-1]
for i in range(n):
    a[i] = ins[i] + des[i] - 1
print(max(a))