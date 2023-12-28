import sys
# strip은 양쪽 공백을 삭제함 

while True: 
    n = sys.stdin.readline().strip()
    if n == '0':
        break

    n = list(n)

    if n==list(reversed(n)):
        print('yes')
    else:
        print('no')