def solution(t, p):
    answer = 0 # 갯수를 셈
    cnt = len(p) # p의 길이
    for i in range(len(t)):
        if i + cnt > len(t):
            break
        
        if int(p) >= int(t[i:i+cnt]):
            answer += 1
    
    return answer