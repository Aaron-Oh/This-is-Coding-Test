import sys

input = sys.stdin.readline

coords = list(input())
column = ord(coords[0]) - 96
row = int(coords[1])

routes = [[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]
cnt = 0
for route in routes:
    tmpCol = column + route[0]
    tmpRow = row + route[1]
    if tmpCol > 0 and tmpCol <= 8 and tmpRow > 0 and tmpRow <= 8:
        cnt += 1
print(cnt)
