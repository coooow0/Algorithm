# 영식 요금제: 30초마다 10원씩 청구, 30초 이하를 사용해도 10원/ 30~59초는 20원 y
# 민식 요금제: 60초마다 15원, 60~119 30원 m

n = int(input())
y, m = 0, 0
arr = list(map(int, input().split()))
for i in range(n):
    y += (arr[i] // 30 + 1) * 10 # 반올림 함수 math.ceil()
    m += (arr[i] // 60 + 1) * 15
if y > m: # m이 저렴할 경우
    print('M', m)
elif y < m: # y가 저렴할 경우
    print('Y', y)
else:
    print('Y M', y)