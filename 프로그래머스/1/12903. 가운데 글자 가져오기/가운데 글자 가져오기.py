def solution(s):
    mid = len(s) // 2
    if len(s) % 2 == 0: #짝수의 경우
        return s[mid-1:mid+1]
    else:
        return s[mid]
