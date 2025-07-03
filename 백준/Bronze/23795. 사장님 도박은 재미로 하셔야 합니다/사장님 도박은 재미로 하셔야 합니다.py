import sys
input = sys.stdin.readline

cnt = 0

while True:
    money = int(input().strip())
    if money == -1:
        print(cnt)
        break
    
    cnt += money