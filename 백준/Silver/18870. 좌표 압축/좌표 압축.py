# 좌표 압축 -> 지금 현재 수보다 작은 수를 찾음 == 내가 몇번째로 작은지

import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
s = set(arr) #중복 제외한 개수를 세야댐
s = sorted(list(s))

dic = dict()

# 인덱스 = 내가 몇번째로 작은가!!!! 
for i in range(len(s)):
    dic[s[i]] = i

for i in arr:
    print(dic[i], end=" ")