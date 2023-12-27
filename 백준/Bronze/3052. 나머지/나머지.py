test = list()
for i in range(10):
    a = int(input())
    test.append(a%42)
test = set(test)
print(len(test))