def solution(numbers: list, hand: str) -> str:
    answer: str = ''
    left: int = 10
    right: int = 12

    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            left = number
        elif number in [3, 6, 9]:
            answer += 'R'
            right = number
        else:
            number = 11 if number == 0 else number
            leftDist: int = abs(number-left)
            rightDist: int = abs(number-right)
            if sum(divmod(leftDist, 3)) > sum(divmod(rightDist, 3)):
                answer += 'R'
                right = number
            elif sum(divmod(leftDist, 3)) < sum(divmod(rightDist, 3)):
                answer += 'L'
                left = number
            else:
                if hand == 'right':
                    answer += 'R'
                    right = number
                else:
                    answer += 'L'
                    left = number

    return answer

if __name__ == '__main__':
    numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
    hand = 'right'
    print(solution(numbers, hand))
    numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
    hand = 'left'
    print(solution(numbers, hand))
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    hand = 'right'
    print(solution(numbers, hand))