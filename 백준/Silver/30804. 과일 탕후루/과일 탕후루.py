import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().strip().split()))

start = 0 # 탕후루 개수 세기
fruits_count = {} # 과일 종류를 셀 딕셔너리
max_len = 0 # 최대 길이

for end in range(n):
    last = arr[end]
    
    if arr[end] in fruits_count: # 같은 종류의 과일이 있으면 개수만 추가하기
        fruits_count[last] += 1
    else: # 없으면 과일 개수를 1로 정해주기
        fruits_count[last] = 1
        
    while (len(fruits_count) > 2): # 3개 이상의 경우
        first = arr[start]
        fruits_count[first] -= 1 # 
        if fruits_count[first] == 0:
            del fruits_count[first]
            
        start += 1
    
    max_len = max(max_len, end - start + 1)

print(max_len)
