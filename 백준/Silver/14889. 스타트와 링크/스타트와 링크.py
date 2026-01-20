import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

from itertools import combinations

n = int(input().strip())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().strip().split())))
    
visited = [False for _ in range(n)]
res = 10000000

def team(cnt, start):
    global res
    
    if cnt == n // 2:
        true_arr = []
        false_arr = []

        for i in range(n):
            if visited[i]:
                true_arr.append(i)
            else:
                false_arr.append(i)
                
        # 각 배열의 숫자들로 permutations 해서 합 구함. 
        true_res=0
        false_res=0
        # for i in permutations(true_arr, 2):
        #     arr = list(i)
        #     true_res += graph[arr[0]][arr[1]]
            
        # for i in permutations(false_arr, 2):
        #     arr = list(i)
        #     false_res += graph[arr[0]][arr[1]]
        
        for i in combinations(true_arr, 2):
            arr = list(i)
            true_res += graph[arr[0]][arr[1]] + graph[arr[1]][arr[0]]

        for i in combinations(false_arr, 2):
            arr = list(i)
            false_res += graph[arr[0]][arr[1]] + graph[arr[1]][arr[0]]
        
        
        res = min(res, abs(true_res - false_res))
        
        return # 결과값 찾으면 return
    
    
    for i in range(start, n):
        if not visited[i]:
            # 아직 방문 안했으면 = False면
            visited[i] = True
            team(cnt + 1, i) # i를 넘겨줌. 여기까지는 세었으니, 다음 재귀에서는 이 뒤부터 확인혀
            visited[i] = False

# team(0, 0)
visited[0] = True # 0번을 고정하면 어느 한 팀에 속하게 됨. 가능한 모든 팀의 조합을 다 찾음. 
# 근데 0번이 링크 팀이면 스타트팀이었을 때 상황을 또!! 확인하게 됨. 
team(1, 1)
print(res)
