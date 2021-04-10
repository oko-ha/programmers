import re

def solution(dartResult):
    answer = temp = 0
    dartResult = re.sub('([0-9]0?)',' \\1',dartResult)
    rlist = re.split(' ',dartResult)
    print('rlist:', rlist)
    for i in range(1, 4):
        number = 0
        bonus = 1
        word = symbol = ''
        for j in rlist[i]:
            if j.isdigit():
                if number != 0:
                    number = number * 10 + int(j)
                else:
                    number = int(j)
            elif j.isalpha():
                word = j
            else:
                symbol = j
        if symbol == '*':
            bonus = 2
            answer += temp
        elif symbol == '#':
            bonus = -1
        if word == 'S':
            temp = number * bonus
        elif word == 'D':
            temp = number ** 2 * bonus
        elif word == 'T':
            temp = number ** 3 * bonus

        answer += temp
        print(answer)
        

    return answer

key = '1D2S#10S'
print('answer:', solution(key))
