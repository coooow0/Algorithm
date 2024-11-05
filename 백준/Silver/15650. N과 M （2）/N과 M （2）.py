n, m = map(int, input().split())

arr = [0]
def dfs():
    if len(arr) - 1 == m:
        print(' '.join(map(str, arr[1:])))
        return
    
    for i in range(1, n + 1):
        if arr[-1] < i and i not in arr:
            arr.append(i)
            dfs()
            arr.pop()
            
dfs()