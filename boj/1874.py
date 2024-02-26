def solution(target):
    stack = []
    result = []
    count = 1
    for i in target:
        while count <= i:
            stack.append(count)
            count += 1
            result.append('+')
        if stack[-1] == i:
            stack.pop()
            result.append('-')
        else:
            return 'NO'

    return '\n'.join(result)

def getUserInput():
    n = int(input())
    target = []
    for _ in range(n):
        target.append(int(input()))

    return target

if __name__ == '__main__':
    target = getUserInput()
    print(solution(target))
