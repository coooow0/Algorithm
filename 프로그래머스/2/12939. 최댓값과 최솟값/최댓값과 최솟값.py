def solution(s):
    s = list(map(int, s.split(' ')))
    answer = str(min(s)) + ' ' + str(max(s))
    return answer