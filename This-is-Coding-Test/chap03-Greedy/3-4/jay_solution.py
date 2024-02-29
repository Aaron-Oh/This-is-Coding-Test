#######################
#### Until being 1 ####
#######################
import sys
input = sys.stdin.readline

def getUserInput():
    n, k = map(int, input().split())
    if isValidInput(n, k): return n, k
    else: raise Exception("Invalid Input")

def isValidInput(n:int, k:int) -> bool:
    if not (1 < n, k < 100001): return False
    return True

def solution(n:int, k:int) -> int:
    count = 0
    while n > 1:
        n = n // k if n % k == 0 else n - 1
        print(n)
        count += 1
    return count

if __name__ == "__main__":
    n, k = getUserInput()
    print(solution(n, k))
