# 트리순회

import sys
input = sys.stdin.readline

n = int(input().strip())
node = {}
for _ in range(n):
    root, left, right = map(str, input().strip().split())
    node[root] = [left, right]
    
def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(node[root][0]) # 왼쪽 노드 탐색
        preorder(node[root][1]) # 오른쪽 노드 탐색

def inorder(root):
    if root != '.':
        inorder(node[root][0])
        print(root, end='')
        inorder(node[root][1])

def postorder(root):
    if root != '.':
        postorder(node[root][0])
        postorder(node[root][1])
        print(root, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')