s = input()
croa = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in croa:
    s = s.replace(i, '*')
print(len(s))