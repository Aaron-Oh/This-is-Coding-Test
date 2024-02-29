import sys

input = sys.stdin.readline
N = int(input())

total = (N + 1) * 3600
cnt = 0
for i in range(total):
    hour = i // 3600
    if "3" in list(str(hour)):
        cnt += 1
        continue
    minute = i % 3600 // 60
    if "3" in list(str(minute)):
        cnt += 1
        continue
    second = i % 60
    if "3" in list(str(second)):
        cnt += 1
        continue

print(cnt)
