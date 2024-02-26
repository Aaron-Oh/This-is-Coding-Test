import sys
input = sys.stdin.readline

def getUserInput() -> list:
    n: int = int(input())
    response: list = []

    for _ in range(n):
        num = input().rstrip().split('.')
        response.append(int(num[0])*1000 + int(num[1]))
    return response

def verify(checker: int, input: int) ->  bool:
    flag: bool = False

    if input*checker % 1000 == 0:
        flag = True
    if input*checker // 1000 != (input + 0.9)*checker // 1000:
        flag = True
    return flag

def listCheck(flag: list) -> bool:
    for i in range(len(flag)):
        if not flag[0][i]:
            return False
    return True

def calculate(input: int, response: list) -> list:
    flag: list = [[False] * len(response)]

    for i in response:
        if listCheck(flag):
            break
        if verify(input, i):
            flag[0][response.index(i)] = True
            print(f'flag: {flag}')
    print(f'return flag: {flag}')
    return flag

def solution(response: list) -> int:
    answer: int = 0

    for i in range(1, 1001):
        if calculate(i, response):
            answer = i
            break
    return answer

if __name__ == '__main__':
    response: list = getUserInput()
    print(solution(response))


"""
There exist some problem with float operations
so it should be careful with taking input
"""