import sys
input = sys.stdin.readline
n = int(input().strip())
log = {}
for i in range(n):
    name, data = map(str, input().split())
    if data == 'enter':
        log[name] = data
    else:
        del log[name]

log = sorted(log, reverse=True)
for i in log:
    print(i)