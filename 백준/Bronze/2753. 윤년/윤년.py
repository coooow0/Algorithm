n = int(input())
if (n % 4) == 0 and ((n % 100) != 0 or n % 400 == 0):
    print(1)
else:
    print(0)