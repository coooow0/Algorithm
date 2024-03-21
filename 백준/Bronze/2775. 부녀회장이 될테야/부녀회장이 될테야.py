import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    height = int(input()) # 층
    weight = int(input()) # 호
    people = [ i for i in range(1, weight+1)]
    # people 에 1부터 n+1까지 채워넣음
    
    for i in range(1, height+1):
        for j in range(1, weight):
            people[j] += people[j-1]
    print(people[weight-1])
