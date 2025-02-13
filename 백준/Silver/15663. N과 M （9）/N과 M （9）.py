import sys
input = sys.stdin.readline

def dfs():
    if len(ans) == m:
        print(*ans)
        return
    
    pre = -1 # 이전에 사용한 숫자를 저장하기 위해 만듦
    
    for i in range(n):
        if not visited[i] and pre != arr[i]:
            visited[i] = True
            ans.append(arr[i])
            pre = arr[i] # 갱신해주기
            
            dfs()
            
            ans.pop()
            visited[i] = False
        
    

n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr.sort()

ans = [] # 정답 저장 배열
visited = [False] * n
# 방문을 했는지 안 했는지 확인하여 건너뛰기

dfs()