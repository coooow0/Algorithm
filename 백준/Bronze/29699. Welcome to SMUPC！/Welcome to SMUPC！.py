# 29699

import sys
input = sys.stdin.readline

n = int(input())
line = 'WelcomeToSMUPC'

if n > 14:
    print(line[n % 14 - 1])
else:
    print(line[n - 1])