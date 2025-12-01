import sys
input = sys.stdin.readline

sab = int(input())
ma, fab, mb = map(int, input().split())

# 4시간 이하 구간의 경우 고속철도가 더 우위임. 아니면 항공이고
# 
if sab <= 240 or sab <= ma + fab +mb:
    print('high speed rail')
else:
    print('flight')