import sys

input = sys.stdin.readline

N, M = map(int, input().split())

min_nums = []
for _ in range(N):
    row = list(map(int, input().split()))
    min_nums.append(min(row))

print(max(min_nums))
