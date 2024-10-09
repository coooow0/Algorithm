n = int(input())
s = [0] * (n+1)
s[1] = 1
for i in range(2, len(s)):
    s[i] = s[i-1] + s[i-2]

print(s[n])