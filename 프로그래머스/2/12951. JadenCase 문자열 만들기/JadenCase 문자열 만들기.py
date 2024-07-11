# def solution(s):
#     answer = []
#     s = s.split(' ')
#     for i in s:
#         i = i.capitalize()
#         answer.append(i)
        
#     return ' '.join(answer)
def solution(s):
    s = s.lower()
    s = s.split(' ')
    answer = []
    for i in s:
        i = i.capitalize()
        answer.append(i)
    return ' '.join(answer)