##########################
## law of large numbers ##
##########################
import sys
input = sys.stdin.readline

def getUserInput():
    n, m, k = map(int, input().split())
    arr:list = list(map(int, input().split()))

    if isValidInput(n, m, k, arr): return n, m, k, arr
    else: raise Exception("Invalid Input")

def isValidInput(n:int, m:int, k:int, arr:list) -> bool:
    if not (2 <= n <= 1000 and 1 <= m <= 10000 and 1 <= k <= 10000): return False
    for i in range(n):
        if not (1 <= arr[i] <= 10000): return False
    if not k <= m: return False

    return True

def solution(m:int, k:int, arr:list)->int:
    arr.sort(reverse=True)
    first = arr[0]
    second = arr[1]
    cnt = 0
    cnt += (m // (k+1)) * k
    cnt += m % (k+1)
    return cnt * first + (m-cnt) * second


if __name__ == '__main__':
    n, m, k, arr = getUserInput()
    print(solution(m, k, arr))