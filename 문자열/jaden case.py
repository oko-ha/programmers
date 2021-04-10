def jaden_case(s):
    answer = ''
    temp = []
    lst = s.lower().split(' ')
    print(lst)
    for i in lst:
        temp.append(i.capitalize())

    return ' '.join(temp)

def solution(s):
    return s.title()

s = "3people unFollowed me"
print(jaden_case(s))
