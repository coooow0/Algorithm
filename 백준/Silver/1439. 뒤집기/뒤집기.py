arr = input()
A = list(map(str, arr.split('1')))
A = [i for i in A if i != '']
B = (list(map(str, arr.split('0'))))
B = [i for i in B if i != '']
# print(min(A, B))

print(min(len(A), len(B)))