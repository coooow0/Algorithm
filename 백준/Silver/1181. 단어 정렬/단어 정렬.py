n = int(input())
arr = list()
for _ in range(n):
    arr.append(input())
list_set = set(arr) #set = 집합 자료형, 중복 허가 안함. 그러나 순서가 뒤죽박죽 될 수 있음
arr = list(list_set) # 다시 리스트로 변환
arr.sort() # 알파벳 순서로 정리
arr.sort(key=len) # 문자열 길이순으로 정리
for i in arr: 
    print(i)