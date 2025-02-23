e, s, m = map(int, input().split())
year = 1

while True:
    if (year - e) % 15 == 0 and (year - s) % 28 == 0 and (year - m) % 19 == 0:
        print(year)
        break
    year += 1