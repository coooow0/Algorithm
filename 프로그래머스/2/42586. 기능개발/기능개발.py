def solution(progresses, speeds):
    end = [] # 며칠만에 종료가 되는지
    answer = [] # 정답 반환 배열
    
    for i in range(len(progresses)):
        if (100 - progresses[i]) % speeds[i] != 0:
            end.append((100 - progresses[i]) // speeds[i] + 1)
        else:
            end.append((100 - progresses[i]) // speeds[i])
            
    cnt = 1
    
    first = end[0]
    
    for num in end[1:]:
        if first < num:
            first = num 
            answer.append(cnt)
            cnt = 1
        else:
            cnt += 1
    
    answer.append(cnt)
    return answer