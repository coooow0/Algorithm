import sys
n = int(sys.stdin.readline())
age = []
for _ in range(n):
    age.append(list(sys.stdin.readline().strip().split()))
age.sort( key = lambda x : int(x[0]))
#sorted: 원본 값은 건들지 않음. sort는 원본을 건드림

for i in range(n):
    print(age[i][0], age[i][1])
