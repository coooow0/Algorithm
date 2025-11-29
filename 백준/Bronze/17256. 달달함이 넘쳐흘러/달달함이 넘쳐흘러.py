import sys
input = sys.stdin.readline

ax, ay, az = map(int, input().strip().split())
cx, cy, cz = map(int, input().strip().split())

# ax - cz = bz
# cy/ ay = by
# cx - az = bx

print(cx - az, cy // ay, cz - ax)