def dfs(start):
    if len(ans) == m:
        print(*ans)
        return 
    
    for i in range(start, len(arr)):
        ans.append(arr[i])
        dfs(i)
        ans.pop()

n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr.sort()
ans = []

dfs(0)