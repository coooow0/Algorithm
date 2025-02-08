import sys
input = sys.stdin.readline

def dfs(start):
    if len(ans) == m:
        print(*ans)
        return 
    
    for i in range(start, n):
        ans.append(arr[i])
        dfs(i + 1)
        ans.pop()
        

n, m = list(map(int, input().split()))
arr = sorted(list(map(int, input().split())))

ans = []
dfs(0) # 몇 번째 원소인지!!