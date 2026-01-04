import sys
input = sys.stdin.readline

n, k = map(int, input().strip().split())
# n은 총 학생, k는 한 방의 최대 인원 수

stu = [[0 for _ in range(2)] for _ in range(6)]
for _ in range(n):
    s, y = map(int, input().strip().split())
    # 성별, 학년. 학년은 한 수 크게 받앗음
    stu[y-1][s] += 1

room = 0

for i in range(6):
    for j in range(2):
        if stu[i][j] % k == 0:
            room += stu[i][j] // k
        else:
            room += stu[i][j] // k + 1
print(room)