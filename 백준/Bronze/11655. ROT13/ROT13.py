import sys
input = sys.stdin.readline().rstrip

s = list(input())
alpha = 26

for i in range(len(s)):
    answer = ord(s[i])
    
    if answer == ord(' ') or (answer >= ord('0') and answer <= ord('9')):
        answer = ord(s[i])
    
    elif answer >= ord('a') and answer <= ord('z'): #소문자일 경우
        answer += 13
        if answer > ord('z'):
            answer -= 26
    else:
        answer += 13
        if answer > ord('Z'):
            answer -= 26

    s[i] = chr(answer)

for i in s:
    print(i, end='')