def solution(participant, completion):
    # 마라톤에 참여한 선수들의 이름이 담긴 배열 participant 
    # 완주한 선수들이 있는 배열 completion
    answer = ""
    participant.sort()
    completion.sort()
    for i, j in zip(participant, completion):
        if i != j:
            return i
    return participant[-1]