####################
#### 숫자 카드 게임 ####
####################
import sys
input = sys.stdin.readline

def getUserInput():
    n, m = map(int, input().split())
    arr:list = [list(map(int, input().split())) for _ in range(n)]

    if isValidInput(n, m, arr): return n, m, arr
    else: raise Exception("Invalid Input")

def isValidInput(n:int, m:int, arr:list) -> bool:
    if not (2 <= n <= 100 and 2 <= m <= 100): return False
    for i in range(n):
        for j in range(m):
            if not (1 <= arr[i][j] <= 10000): return False
    return True

def solution(arr:list)->int:
    minList = [min(row) for row in arr]
    return max(minList)

if __name__ == '__main__':
    n, m, arr = getUserInput()
    print(solution(arr))
