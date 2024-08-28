def solution(numlist, n):
    numlist.sort(key=lambda x: (abs(x - n), -x))
    # x를 abs(x - n) 값에 따라 정렬. 동일할 경우 -x를 기준으로 정렬 
    # 즉, 본래 x의 값이 클수록 우선순위가 높다. 
    answer = []
    for i in numlist:
        answer.append(i)
    return answer 