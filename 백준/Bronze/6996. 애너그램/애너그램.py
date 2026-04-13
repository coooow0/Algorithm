import math
import sys
input = sys.stdin.readline


t = int(input().strip())
for _ in range(t):
    a_dic = dict()
    b_dic = dict()
    
    for i in range(ord('a'), ord('z') + 1):
        a_dic[chr(i)] = 0
        b_dic[chr(i)] = 0
    
    a, b = list(input().strip().split())
    
    for i in a:
        a_dic[i] += 1
    
    for i in b:
        b_dic[i] += 1
    
    res = True
    
    for i in a_dic:
        if a_dic[i] != b_dic[i]:
            res = False
            break
        
    if res:
        print(a, '&', b, 'are anagrams.')
    else:
        print(a, '&', b, 'are NOT anagrams.')
    