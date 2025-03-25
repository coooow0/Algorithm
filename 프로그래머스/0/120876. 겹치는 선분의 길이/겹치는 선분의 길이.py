def solution(lines):
    answer = 0
    cnt = [0] * 201
    for i in range(len(lines)):
        a, b = lines[i][0], lines[i][1]
        for k in range(a, b):
            cnt[k + 100] += 1
    
    for c in cnt:
        if c >= 2: answer += 1
    return answer