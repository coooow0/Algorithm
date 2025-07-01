# 숫자카드
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

m = int(input())
brr = list(map(int, input().split()))

dic = dict()

for a in arr:
    if a in dic:
        dic[a] += 1
    else:
        dic[a] = 1 
        # 1로 초기화를 시킴.. 있으니께
        # arr과 brr에 겹치는 숫자 카드의 개수를 나타내야되니까.. 다 세버림
        # list.count()는 O(n) 이라서... 안된다는데 비슷한 거 같음데
    
for b in brr:
    if b in dic:
        print(dic[b], end =" ")
    else:
        print(0, end=" ")
