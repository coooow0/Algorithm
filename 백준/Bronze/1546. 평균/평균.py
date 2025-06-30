import sys
input = sys.stdin.readline

n = int(input())
score = list(map(int, input().split()))
m = max(score)

for i in range(n):
    score[i] = score[i]/m*100

print(sum(score)/n)

