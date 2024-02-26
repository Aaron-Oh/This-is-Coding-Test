import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
num_arr = list(map(int, input().split()))

num_arr.sort()
sum = 0
max1 = num_arr.pop()
max2 = num_arr.pop()
tmp = 0
cnt = 0
while cnt < M:
    if tmp == K:
        tmp = 0
        sum += max2
    else:
        tmp += 1
        sum += max1
    cnt += 1

print(sum)