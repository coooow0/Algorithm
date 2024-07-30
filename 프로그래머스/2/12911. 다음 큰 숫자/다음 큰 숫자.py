def solution(n):
    a = bin(n)[2:]
    for i in range(n+1, 1000000):
        b = bin(i)[2:]
        if a.count('1') == b.count('1'):
            answer = i
            break
    return answer