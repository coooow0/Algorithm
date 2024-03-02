# 낮에 A미터 갈 수 있음
# 근데 밤에 B미터 미끄러짐
# 정상 V미터~
a, b, v = map(int, input().split())
# 올라가야 하는 높이 V - B 
# 하루에 A - B 올라갈 수 있음 

if (v - b) % (a - b) == 0:
    print((v-b)//(a-b))
else :
    print((v-b)//(a-b)+1)