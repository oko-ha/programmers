def binary(b):
    for i in range(len(b) - 1, -1, -1):
        if b[i] == '0':
            b[i] = '1'
            if i + 1 < len(b):
                b[i + 1] = '0'
            return ''.join(b)
    b[0] = '0'
    return '1' + ''.join(b)
    

def solution(numbers):
    answer = []
    for number in numbers:
        b = binary(list(bin(number)[2:]))
        a = 0
        for i, digit in enumerate(b):
            a += int(digit) * pow(2, len(b) - 1 - i)
        answer.append(a)
    return answer

numbers = [2, 7]
print(solution(numbers))