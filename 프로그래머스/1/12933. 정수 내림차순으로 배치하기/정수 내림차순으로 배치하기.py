def solution(n):
    answer = list(str(n))
    answer.sort(reverse=True)
    answer = "".join(answer)
    return int(answer)