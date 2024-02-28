import sys

input = sys.stdin.readline
N = int(input())
direction_arr = list(input().split())

coord = [1, 1]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for direction in direction_arr:
    y, x = coord
    if direction == "L":
        x = x + dx[0] if x + dx[0] > 0 else x
    elif direction == "R":
        x = x + dx[1] if x + dx[1] <= N else x
    elif direction == "U":
        y = y + dy[2] if y + dy[2] > 0 else y
    elif direction == "D":
        y = y + dy[3] if y + dy[3] <= N else y
    coord = [y, x]

print(coord[0], end=" ")
print(coord[1])
