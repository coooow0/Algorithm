n = int(input())
cnt, room = 1, 1
while n > room:
    room = room + (6 * cnt)
    cnt += 1
print(cnt)