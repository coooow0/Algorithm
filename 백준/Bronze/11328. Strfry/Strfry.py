import sys
input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    a, b = map(str, input().strip().split())
    a = list(a)
    b = list(b)
    
    corr = True
    
    if len(a) != len(b):
        print('Impossible')
        continue
    dic = dict()
    
    for i in a:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    
    for i in dic.keys():
        if dic[i] != b.count(i):
            corr = False
            break
    
    print('Possible' if corr else 'Impossible')