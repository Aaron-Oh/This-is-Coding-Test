###############################
#### Top-Bottom-Left-Right ####
###############################

import sys
input = sys.stdin.readline

def getUserInput():
    n: int = int(input())
    plan:list = list(input().split())
    if verifyInput(n, plan): return n, plan
    print("Invalid Input")

def verifyInput(n:int, plan:list)->bool:
    if n < 1 or n > 100: return False
    if len(plan) < 1 or len(plan) > 100: return False

    return True

def move(n:int, plan:list)->list:
    x, y = 1, 1
    type = ['U', 'D', 'L', 'R']
    nx = [-1, 1, 0, 0]
    ny = [0, 0, -1, 1]

    for i in plan:
        for idx, j in enumerate(type):
            if i == j:
                x += nx[idx]
                y += ny[idx]
                if verifyPosition(x, y, n): continue
                else:
                    x -= nx[idx]
                    y -= ny[idx]

    return x, y

def verifyPosition(x:int, y:int, n:int)-> bool:
    if x < 1 or y < 1: return False
    if x > n or y > n: return False

    return True

if __name__ == '__main__':
    n, plan = getUserInput()
    print(move(n, plan))





