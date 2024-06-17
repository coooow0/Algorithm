nan = []
for i in range(9):
    nan.append(int(input()))
nan.sort()

for i in range(len(nan)):
    for j in range(i):
        if nan[i] + nan[j] == sum(nan) - 100:
            if i > j:
                nan.remove(nan[i])
                nan.remove(nan[j])
            else:
                nan.remove(nan[j])
                nan.remove(nan[i])
            break
    if sum(nan) == 100:
        break
for i in nan:
    print(i)
