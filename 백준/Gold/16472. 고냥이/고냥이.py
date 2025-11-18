import sys
input = sys.stdin.readline

n = int(input().strip())

arr = list(input().strip())

dic = {}
start = 0

max_len = 0

for end in range(len(arr)):
    last = arr[end]
    
    if last not in dic: # 없으면 만들고 있으면 개수 추가
        dic[last] = 1
    else:
        dic[last] += 1 
        
    
    while len(dic) > n: # 최대 개수보다 많으면 다 빼버리
        first = arr[start]
        dic[first] -= 1
        
        if dic[first] == 0:
            del dic[first]
            
        start += 1
    
    max_len = max(max_len, end - start + 1)

print(max_len)