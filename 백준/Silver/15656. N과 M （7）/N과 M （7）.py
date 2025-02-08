
def dfs(start):
    if len(ans) == m:
        print(*ans)
        return 
    
    for i in range(n):
        ans.append(arr[i])
        dfs(i)
        ans.pop()

n, m = list(map(int, input().split()))
arr = sorted(list(map(int, input().split())))

ans = []
dfs(0)