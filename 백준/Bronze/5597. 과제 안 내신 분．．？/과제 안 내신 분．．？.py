import sys
stu = [0] * 31 # 30 + 1
for i in range(28):
    stu[int(sys.stdin.readline())] = 1
for i in range(1, 31):
    if stu[i] == 0:
        print(i)