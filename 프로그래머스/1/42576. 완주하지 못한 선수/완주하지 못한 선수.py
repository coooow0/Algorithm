def solution(participant, completion):
    answer = ""
    sum = {}
    for i in participant:
        if i in sum:
            sum[i] += 1
        else:
            sum[i] = 1
        
    for i in  completion:
        if i in sum:
            sum[i] -= 1
    
    for i in sum:
        if sum[i] != 0:
            answer += i
    return answer