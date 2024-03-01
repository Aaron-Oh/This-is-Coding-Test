import sys

input = sys.stdin.readline

N, M = map(int, input().split())
X, Y, startDir = map(int, input().split())

total_map = []
for _ in range(N):
    total_map.append(list(map(int, input().split())))

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

total_cnt = 1
def checkAvailable(X, Y):
    cases = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    cnt = 0
    for case in cases:
        tmpX = X + case[0]
        tmpY = Y + case[1]
        if total_map[tmpX][tmpY] == 0:
            cnt += 1
    return True if cnt > 0 else False


while checkAvailable(X, Y):
    total_cnt += 1
    total_map[X][Y] = 1
    for i in range(4):
        tmpX = X + dx[i]
        tmpY = Y + dy[i]
        if total_map[tmpX][tmpY] == 0:
            X = tmpX
            Y = tmpY
            break

print(total_cnt)
