from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque()
    
    for i in range(len(priorities)):
        queue.append((priorities[i], i))
        # 값과 인덱스를 넣어줌
    big = max(priorities)
    
    while True:
        value, idx = queue[0]
        
        if big == value:
            queue.popleft()
            
            answer += 1
            priorities[idx] = 0
            
            big = max(priorities) # 제일 큰 값 갱신
            
            if idx == location:
                return answer
        
        else:
            queue.append(queue.popleft())