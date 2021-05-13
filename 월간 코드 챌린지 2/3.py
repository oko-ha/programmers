import re
import sys
import bisect
sys.setrecursionlimit(10**6)
def no111(a):
    for i in range(len(a) -1, -1, -1):
        if a[i] == '0': # 1
            return a[:i+1] + '110' + a[i+1:]
    return '110' + a

def recur(d):
    do1 = re.sub('(110)', '', d)
    length = (len(d) - len(do1)) // 3
    if length == 0: # 110이 없으면
        return d
    else:
        do1 = recur(do1)
        do2 = re.sub('(111)', '110111', do1, 1)
        temp = do2
        index = 1
        while index < length:
            do2 = re.sub('(111)', '110111', temp, 1)
            index += 1
            if temp == do2:
                break
            else:
                temp = do2
        if len(do2) < len(d): # 111이 없으면
            length = (len(d) - len(do2)) // 3
            for _ in range(length):
                do2 = no111(do2)
            return do2
        else: # 111이 있으면
            return do2

def solution(s):
    answer = []
    for st in s:
        answer.append(recur(st))
    return answer

s = ["1110","100111100","0111111010"]
print(solution(s))