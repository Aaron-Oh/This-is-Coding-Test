import sys

input = sys.stdin.readline

def solution():
    n = int(input())
    arr = [500, 100, 50, 10]
    cnt = 0
    for coin in arr:
        cnt += n // coin
        n %= coin
    print(cnt)
if __name__ == "__main__":
    solution()