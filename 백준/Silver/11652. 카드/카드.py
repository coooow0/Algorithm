# 카드
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
brr = list(set(arr)) # 입력받은 배열의 중복값을 없앰. 해시맵 만들기 위해

map = dict()
for i in brr: # 해시맵 초기화
    map[i] = 0
    
for i in arr: # 개수를 셈
    map[i] += 1

answer = 0 # 최대 개수를 세기 위한 변수

for i in map.values(): # 최대 개수를 찾음
    answer = max(i, answer)
    
crr = list() # 같은 개수를 가진 숫자를 집어넣고 작은 것을 고르기 위함
for i in brr: 
    if map[i] == answer:
        crr.append(i)
print(min(crr))