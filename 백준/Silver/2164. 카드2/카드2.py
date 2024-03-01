from collections import deque 
#deque 는 양방향 추가/삭제 가능
n = int(input())
queue = deque(range(1, n+1))
#n까지 리스트에 저장
# print(queue)
while len(queue) != 1:
    queue.popleft() #popleft 맨 앞 값을 삭제함
    queue.append(queue.popleft()) #맨 앞에 있는 값을 뒤에 추가함
    #queue.popleft()는 삭제하기 전 값을 반환함
    #그래서 삭제 후 반환-> 그 값을 뒤에 추가함 이렇게 되는 것

print(queue.popleft())
