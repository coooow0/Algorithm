import sys
input = sys.stdin.readline
sab = int(input().strip())
fab = int(input().strip())

print('high speed rail'if sab <= fab else 'flight')