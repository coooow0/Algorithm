def solution(n):
    answer = -1
    n = n ** 0.5
    if n % 1 == 0:
        return (n+1) ** 2
    return -1
