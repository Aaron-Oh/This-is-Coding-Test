###############################
#### Top-Bottom-Left-Right ####
###############################

import sys
input = sys.stdin.readline

def getUserInput():
    n:int = int(input())
    if verifyInput(n): return n
    else: print("Please write down 0 to 23 integer")

def verifyInput(n:int)->bool:
    if n < 0 or n > 24 : return False
    return True

def solution(n:int)->int:
    cnt:int = 0
    for i in range(n + 1):
        for j in range(60):
            for k in range(60):
                if '3' in str(i)+str(j)+str(k): cnt += 1

    return cnt


if __name__ == '__main__':
    print(solution(getUserInput()))
