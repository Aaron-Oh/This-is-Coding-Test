###############################
#### Royal Knight ####
###############################
import sys
input = sys.stdin.readline

def getUserInput():
    position:list = list(input())

    if verifyInput(position):
        position[0] = ord(position[0]) - 96
        position[1] = int(position[1])
        return position
    else: print("Invalid Input")

def verifyInput(input:list)->bool:
    if ord(input[0]) < 97 or ord(input[0]) > 105: return False
    if int(input[1]) < 0 or int(input[1]) > 8: return False

    return True

def verifyMove(x:int,y:int, step:list)->bool:
    if x + step[1] < 1 or x + step[1] > 8: return False
    if y + step[0] < 1 or y + step[0] > 8: return False
    return True

def moveKnight(input:list)->int:
    answer:int = 0
    steps: list = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]
    x, y = input[0], input[1]

    for step in steps:
        if verifyMove(x, y, step): answer += 1

    return answer

if __name__ == '__main__':
    print(moveKnight(getUserInput()))
