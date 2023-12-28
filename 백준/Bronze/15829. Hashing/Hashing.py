import sys
input = sys.stdin.readline

#아스키 코드에서 a는 97이지만 여기선 1임

t = int(input())
str_L = input()
list = list(str_L)
result = 0
for i in range(t):
    result += ((ord(list[i])-96) * pow(31, i))
print(result)