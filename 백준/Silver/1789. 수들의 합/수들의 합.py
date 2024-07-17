s = int(input())
answer = 0
for i in range(1, 1000000):
    answer += i
    if answer > s:
        print(i-1)
        break