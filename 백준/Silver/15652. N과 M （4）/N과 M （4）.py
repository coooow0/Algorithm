import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())

arr = [0]

def dfs():
    if len(arr) - 1 == m:
        print(' '.join(map(str, arr[1:])))
        return
    
    for i in range(1, n+1):
        if arr[-1] <= i:
            arr.append(i)
            dfs()
            arr.pop()
            
dfs()