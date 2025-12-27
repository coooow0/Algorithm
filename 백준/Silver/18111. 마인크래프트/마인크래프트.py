# 높이 0~256까지 다 확인하기.. 이런 ㅁㅊ 
import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
# n개의 줄에 m개의 정수로 땅의 높이가 주어짐. 
# b는 인벤토리의 블록 수

graph = []

dic = {} # 높이 개수 세기

for i in range(n):
    graph.append(list(map(int, input().split())))
    for k in graph[i]:
        if k in dic:
            dic[k] += 1
        else:
            dic[k] = 1
     
# 1. 0부터 256까지 다 탐색.  
sec = 500 * 500 * 256 * 2
height = 0

for i in range(257):
    inv = b # 인벤토리 개수
    cur_time = 0 # 현재 시간
    
    for r in dic:
        # 여기서 r은 땅의 높이이고, dic[r]은 그 땅의 개수임. .염병
        if r < i: 
            # 목표하는 땅의 높이가 더 높을 경우, 인벤에서 꺼내 써야댐. 
            cur_time += (i - r) * dic[r]# 현재 시간 = 뺀 블럭의 수 * 해당 칸의 수
            inv -= (i - r) * dic[r]
            
        elif r > i:
            cur_time += 2 *(r - i) * dic[r]            
            inv += (r - i) * dic[r]
    
    if inv >= 0:
        if sec >= cur_time:
            sec = cur_time 
            height = max(height, i)
            
print(sec, height)