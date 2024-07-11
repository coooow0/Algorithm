def solution(s):
    cnt = 0 # 2진수 횟수
    zero = [] # 0의 개수
    one = []
    s = list(map(int, s))
    for i in s:
        if i == 1:
            one.append(1)
        else:
            zero.append(0)

    while True:
        s = list(map(int, bin(len(one))[2:]))
        cnt += 1
        if len(s) == 1 and s[0] == 1:
            break

        one = []
        for i in s:
            if i == 1:
                one.append(1)
            else:
                zero.append(0)
    answer = [cnt, len(zero)]
    return answer