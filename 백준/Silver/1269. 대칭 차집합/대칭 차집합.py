n, m = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))


def count(a, b):
    res = 0
    for i in a:
        if i not in b:
            res += 1
    return res

cnt = 0
cnt += count(A, B)
cnt += count(B, A)
print(cnt)