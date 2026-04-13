import math
import sys
input = sys.stdin.readline

n = int(input().strip())
arr = list(map(int, input().strip().split()))

# 각 마을에서 마을까지의 이동 비용이 주어질 때, 
# 최소한의 이동비용으로 섬 모든 마을 관광하려면 얼만의 이동비용을 준비?

arr.sort()

print(sum(arr[:n - 1]))