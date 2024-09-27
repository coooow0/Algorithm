import sys
input = sys.stdin.readline().rstrip
s = input()
arr = [''] * len(s)
for i in range(len(s)):
    answer = ''
    for k in range(i, len(s)):
        answer += s[k]
    arr[i] = answer
arr.sort()
for i in arr:
    print(i)