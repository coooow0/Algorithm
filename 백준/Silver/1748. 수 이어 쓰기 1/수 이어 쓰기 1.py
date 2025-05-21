n = input()
nine = 0

if int(n) < 10:
    print(n)
else:
    for i in range(len(n)-1):
        nine += 9 * 10 ** i * (i + 1)
    print(nine + (int(n) - 10 ** (len(n) - 1) + 1) * len(n))