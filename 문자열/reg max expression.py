import re
import itertools
import copy
def max_expression(expression):
    answer = []
    comb = set(re.findall('[-+*]', expression))
    operator_list = list(itertools.permutations(comb, len(comb)))
    print(operator_list) #
    division = re.split('([-+*])', expression)
    print(division) #
    for operator in operator_list:
        temp = copy.deepcopy(division)
        for op in operator:
            i = 1
            while len(temp) > 1 and i < len(temp):
                if op == temp[i]:
                    temp[i-1] = str(eval(temp[i-1]+op+temp[i+1]))
                    del temp[i:i+2]
                else:
                    i += 1
        answer.append(abs(int(temp[0])))

    print(answer) #
    
    return max(answer)

def solution(expression):
    #1
    op = [x for x in ['*','+','-'] if x in expression]
    op = [list(y) for y in permutations(op)]
    ex = re.split(r'(\D)',expression)

    #2
    a = []
    for x in op:
        _ex = ex[:]
        for y in x:
            while y in _ex:
                tmp = _ex.index(y)
                _ex[tmp-1] = str(eval(_ex[tmp-1]+_ex[tmp]+_ex[tmp+1]))
                _ex = _ex[:tmp]+_ex[tmp+2:]
        a.append(_ex[-1])

    #3
    return max(abs(int(x)) for x in a)

expression = "100-200*300-500+20"
print(max_expression(expression))
