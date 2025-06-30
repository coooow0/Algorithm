# 웰컴 키트
import math
n = int(input()) # 참가자 수
# 사이즈별 신청자의 수
shirts = list(map(int, input().split())) 

# 티셔츠와 펜의 묶음 수
T, P = map(int, input().split())

t_cnt = 0

for i in shirts:
    if i > 0:
        t_cnt += math.ceil(i / T)
        
print(t_cnt)
print(n // P, n % P)