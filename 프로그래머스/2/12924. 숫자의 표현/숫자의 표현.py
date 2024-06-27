def solution(n):
    answer = 0
    for i in range(1, n+1):
        cnt = 0
        for k in range(i, n+1):
            cnt += k
            if cnt == n:
                answer+=1
                break
            elif cnt > n:
                break
    return answer