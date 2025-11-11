import sys
input = sys.stdin.readline

# 4시간 이하일 경우 고속철도가 더 나음
# 역 a -> 역 b로 갈 때 어떤게 더 나은지,... 
sab = int(input())

ma, fab, mb = map(int, input().strip().split())

if sab <= 240 or sab <= ma + fab + mb:
    print('high speed rail')
else:
    print('flight')