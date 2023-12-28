import sys
input = sys.stdin.readline
#대량을 입력할 때에는 sys.stdin.readline을 사용하는 것이 좋음

t = int(input())
list = list()
for i in range(t):
    a = int(input())
    if a == 0:
        list.pop()
    else:
        list.append(a)
print(sum(list))
