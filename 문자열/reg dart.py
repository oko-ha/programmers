import re

def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    #p = re.compile('(\d+)([SDT])([*#]?)')
    #dart = p.findall(dartResult)
    dart = re.findall('(\d+)([SDT])([*#]?)', dartResult)
    print('dart :', dart)
    print('type :', type(dart))
    for i in range(len(dart)):
        if dart[i][2] == '*':
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]
        print('dart :', dart)
    answer = sum(dart)
    return answer

key = '1D*2S#10S'
print('answer:', solution(key))
