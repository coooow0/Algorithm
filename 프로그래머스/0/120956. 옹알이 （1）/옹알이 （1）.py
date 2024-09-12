def solution(babbling):
    answer = 0        
    ong = ['aya', 'ye', 'woo', 'ma'] # 할 수 있는 옹알이
    for i in babbling:
        for k in ong:
            i = i.replace(k, '-')
        if len(i) == i.count('-'):
            answer += 1


    return answer