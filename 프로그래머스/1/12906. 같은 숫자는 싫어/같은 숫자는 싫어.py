def solution(arr):
    answer = []
    n = -1 # 전의 수
    for i in arr:
        if i != n:
            answer.append(i)
        n = i
    return answer