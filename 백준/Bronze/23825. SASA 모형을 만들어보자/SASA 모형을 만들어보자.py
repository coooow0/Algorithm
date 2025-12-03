# 23825
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# S가 n개, A가 m개 => sasa
# n이랑 m을 2로 나눴을 때 더 작은 값
print(min(n // 2, m // 2))
