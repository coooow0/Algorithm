n = input()
for i in range(97, 123):
    if chr(i) in n:
        print(n.index(chr(i)), end=' ')
    else:
        print(-1, end=' ')
    