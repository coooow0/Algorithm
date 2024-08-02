def solution(n):
    answer = ""
    while n:
        result = n % 3
        if result == 0:
            result = 4
            n -= 1
        answer += str(result)
        n = n // 3
    return answer[::-1]
