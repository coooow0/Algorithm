n = input()

if '0' not in n or sum(map(int, n)) % 3 != 0 :
    print(-1)           
                       
else:
    print(''.join(sorted(n, reverse=True)))