import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pswd = dict()

for _ in range(n):
    site, password = map(str, input().split())
    pswd[site] = password

for _ in range(m):
    site = input().strip()
    print(pswd[site])