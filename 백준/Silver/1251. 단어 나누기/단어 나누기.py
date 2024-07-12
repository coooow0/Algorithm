s = input()
words = []
for i in range(1, len(s) - 1):
    for k in range(i + 1, len(s)):
        s1 = s[:i][::-1]
        s2 = s[i:k][::-1]
        s3 = s[k:][::-1]
        word = s1 + s2 + s3
        words.append(word)
print(min(words))