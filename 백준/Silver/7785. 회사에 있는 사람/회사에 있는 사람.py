n = int(input())
log = {}
for _ in range(n):
    name, data = map(str, input().split())
    log[name] = data

result = []
for i in log:
    if log[i] == 'enter':
        result.append(i)
    # 회사에 있는 사람들만 배열에 넣어줌

result.sort(reverse=True)
# 내림차순으로 정렬

for i in result:
    print(i)