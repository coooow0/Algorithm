score = {'A+': 4.5,
         'A0': 4.0,
         'B+': 3.5,
         'B0': 3.0,
         'C+': 2.5,
         'C0': 2.0,
         'D+': 1.5,
         'D0': 1.0,
         'F': 0
         }
scr_sum = 0 # 각 학점 * 점수
avgscore = 0
for i in range(20):
    s = list(input().split())    
    if s[2] in score:
        scr_sum += float(s[1]) * score[s[2]]
        avgscore += float(s[1])
print(round(scr_sum / avgscore, 6))