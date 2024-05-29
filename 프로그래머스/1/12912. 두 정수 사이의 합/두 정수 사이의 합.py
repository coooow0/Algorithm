def solution(a, b):
    answer = 0
    if a > b:
        temp = a
        a = min(a, b)
        b = max(temp, b+1)
    for i in range(a, b+1):
        answer += i
    return answer